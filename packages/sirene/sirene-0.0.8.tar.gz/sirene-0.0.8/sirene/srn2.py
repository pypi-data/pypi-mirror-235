import pandas as pd
import numpy as np
from iotbr import io_system as ios
from iotbr import tru
from importlib import resources
import io


# 0) functions
def agrega_col(matrix,col1,col2):
  # Sum col and col2
  summed_column = matrix[:, col1] + matrix[:, col2]
  # Replace col1 with (col1+col2)
  matrix[:, col1] = summed_column
  # Exclude col2
  final_matrix = np.delete(matrix, col2, axis=1)
  return final_matrix

def agrega_row(matrix, row1, row2):
  # Sum row1 and row2
  summed_row = matrix[row1, :] + matrix[row2, :]
  # Replace row1 with (row1+row2)
  matrix[row1, :] = summed_row
  # Exclude row2
  final_matrix = np.delete(matrix, row2, axis=0)
  return final_matrix

#apenas transtormar em dataframe
def matrix_to_df(matrix,index_x,index_y):
    df = pd.DataFrame(matrix)
    df = df.set_index(index_y)
    df.index.name = 'setores/produtos'
    df = df.rename(columns={df.columns[i]:index_x[i] for i in  range(len(index_x))})
    return df

# 1) import data about credit
with resources.open_binary('sirene.co2e_and_scr', 'public_data_scr_2012_12_a_2022_12_68TRU.csv') as f:
  data = f.read()
  bytes_io = io.BytesIO(data)
scr = pd.read_csv(bytes_io)

# 1.1) adjust (68 to 67 sectors).
# Saude = saude publica (8691) + saude privada (8692)
scr.loc[scr['atividade_tru68_ibge'] == '8691', 'atividade_tru68_ibge'] = '8691 + 8692'
scr.loc[scr['atividade_tru68_ibge'] == '8692', 'atividade_tru68_ibge'] = '8691 + 8692'

# educacao = educação publica (8591) + educação privada (8592)
scr.loc[scr['atividade_tru68_ibge'] == '8591', 'atividade_tru68_ibge'] = '8591 + 8592'
scr.loc[scr['atividade_tru68_ibge'] == '8592', 'atividade_tru68_ibge'] = '8591 + 8592'

scr_67 = scr.groupby(['ano','cliente','atividade_tru68_ibge'])['sum_carteira_ativa'].sum().reset_index()
scr_67.loc[scr_67['cliente'].str.contains('PF'), 'atividade_tru68_ibge'] = 'RESIDENCIAL'



# 2) import data about emission
with resources.open_binary('sirene.co2e_and_scr', 'emissions_68_sectors_plus_hausehold_Gg_CO2e_GWP_SAR_v1.csv') as f:
  data = f.read()
  bytes_io = io.BytesIO(data)
co2e = pd.read_csv(bytes_io)

# 2.1) total emission
co2e['total_Gg_CO2e_GWP_SAR'] = (co2e['energia_Gg_CO2e_GWP_SAR'] + co2e['residuo_Gg_CO2e_GWP_SAR'] +
                           co2e['agropecuaria_Gg_CO2e_GWP_SAR'] + co2e['ippu_Gg_CO2e_GWP_SAR'] +
                           co2e['lulucf_Gg_CO2e_GWP_SAR'])

# 2.2) adjust (68 to 67 sectors).
# Saude = saude publica (8691) + saude privada (8692)
co2e['atividade_tru68_ibge'] = co2e['index'].str.split('\n').str[0]
co2e.loc[co2e['atividade_tru68_ibge'] == '8691', 'atividade_tru68_ibge'] = '8691 + 8692'
co2e.loc[co2e['atividade_tru68_ibge'] == '8692', 'atividade_tru68_ibge'] = '8691 + 8692'

# educacao = educação publica (8591) + educação privada (8592)
co2e.loc[co2e['atividade_tru68_ibge'] == '8591', 'atividade_tru68_ibge'] = '8591 + 8592'
co2e.loc[co2e['atividade_tru68_ibge'] == '8592', 'atividade_tru68_ibge'] = '8591 + 8592'

# 2.3) group by activity
co2e_67 = co2e.groupby(['year','atividade_tru68_ibge'])[['energia_Gg_CO2e_GWP_SAR',
							 'residuo_Gg_CO2e_GWP_SAR',
							 'agropecuaria_Gg_CO2e_GWP_SAR',
							 'ippu_Gg_CO2e_GWP_SAR',
							 'lulucf_Gg_CO2e_GWP_SAR',
							 'total_Gg_CO2e_GWP_SAR']].sum().reset_index()
 
 
# 3) Estimate 67 activities Leontief matrix
# (68 setores) + (household) - (educação publica + educação privada) + educação - (saúde publica + saúde privada) + saúde = 67 setores
  

class coef: 
    def __init__(self,year,lulucf=True):
        self.year = year
        self.lulucf = lulucf
        self.leontief_inverse_matrix_67()
        self.added_value()
        self.coefficients()
    def leontief_inverse_matrix_67(self):
    	sys = ios.system(self.year,'68','t')
    	#1) estimar matriz demanda intermediária com household (mZBarr)
    	##bens estão nas linhas e setores nas colunas. Cada setor produz um unico bem
    	mZ = sys.mD_int_pb_qua #matris quadrada de demanda intermediádia a preços básicos
    	vVA_table_rem = tru.read_var(sys.Y,sys.L,'VA_table',sys.u)['Remunerações'].values.reshape(-1, 1).T#renda das famílias (=Renda do Trabalho)

    	#modificar a matriz de demanda intermediária
    	##inserir o bem trabalho na última linha da matriz de demanda intermediária
    	mZBarr =  np.concatenate((mZ, vVA_table_rem), axis=0)

    	##inserir setor trabalho na ultima coluna da matriz de demanda intermediária
    	vD_final_pb_qua_C_f = sys.mD_final_pb_qua[:,3]#consumo das famílias a pb
    	vD_final_pb_qua_C_f_ = np.append(vD_final_pb_qua_C_f, 0).reshape(-1, 1)
    	mZBarr = np.concatenate((mZBarr, vD_final_pb_qua_C_f_), axis=1)

    	#2) estimar vetor de valor bruto (produção + household) (vVBP)
    	#Valor bruto da produção
    	vVBP = tru.read_var(sys.Y,sys.L,'VA_table',sys.u)['Valor da produção'].values
    	#print(np.sum(vVBP))

    	#valor bruto do household
    	vVBP_h = np.sum(vVA_table_rem)
    	#print(vVBP_h)

    	#modificar o vetor de valor bruto da produção
    	##inserir o bem trabalho na última linha do vetor
    	vVBP = np.append(vVBP, vVBP_h).reshape(-1, 1).T

    	#3) ajustar mZBarr e vVBP
    	#Lembbre que agora temos que agrupar saude publica + saude privada e
    	#educação pública + educação privada.

    	#3.1) ajustar vetor vVBP
    	#linha = coluna = 68 = household
    	#linha = coluna = 64 = 8692\nSaúde privada
    	#linha = coluna = 63 = 8691\nSaúde pública
    	#linha = coluna = 62 = 8592\nEducação privada
    	#linha = coluna = 61 = 8591\nEducação pública
    	#saude = linha 65 + linha 64
    	vVBP_ = agrega_col(vVBP,61,62)
    	vVBP_ = agrega_col(vVBP_,63,64)

    	#3.2) ajustar matrix mZBarr
    	mZBarr_ = agrega_row(mZBarr ,61,62)
    	mZBarr_ = agrega_row(mZBarr_,63,64)
    	mZBarr_ = agrega_col(mZBarr_,61,62)
    	mZBarr_ = agrega_col(mZBarr_,63,64)

    	#4) Estimar matriz auxiliar A
    	mABarr= np.zeros([int(sys.L)+1-2,int(sys.L)+1-2], dtype=float)
    	mABarr[:,:] = mZBarr_[:,:]  / vVBP_[0,:]

    	#5) reestimar a matriz de Leontief para 67 setores
    	mIBarr = np.eye(int(sys.L) +1 -2 )
    	self.mLeontiefBarr = np.linalg.inv(mIBarr - mABarr)
    	self.sys = sys
    def added_value(self):
    	#1) valor adicionado
    	#valor adicionado (firmas)
    	vVBP_f = tru.read_var(self.sys.Y,self.sys.L,'VA_table',self.sys.u)['Valor da produção']#.values

    	#valor adicionado (familias)
    	vVBP_h = pd.DataFrame(tru.read_var(self.sys.Y,self.sys.L,'VA_table',self.sys.u)['Remunerações']).values.sum()#.shape

    	#valor adicionado (estrutura 69 setores)
    	vVBP_f.loc['RESIDENCIAL'] = vVBP_h
    	vPBP_t =  vVBP_f.copy()


    	# ajustar.
    	vPBP_t = pd.DataFrame(vPBP_t)
    	vPBP_t['atividade_tru68_ibge'] = vPBP_t.index.str.split('\n').str[0]
    	#Saude = saude publica (8691) + saude privada (8692)
    	vPBP_t.loc[vPBP_t['atividade_tru68_ibge'] == '8691', 'atividade_tru68_ibge'] = '8691 + 8692'
    	vPBP_t.loc[vPBP_t['atividade_tru68_ibge'] == '8692', 'atividade_tru68_ibge'] = '8691 + 8692'
    	#educacao = educação publica (8591) + educação privada (8592)
    	vPBP_t.loc[vPBP_t['atividade_tru68_ibge'] == '8591', 'atividade_tru68_ibge'] = '8591 + 8592'
    	vPBP_t.loc[vPBP_t['atividade_tru68_ibge'] == '8592', 'atividade_tru68_ibge'] = '8591 + 8592'

    	# agrupar por atividade
    	vPBP_t_group = vPBP_t.groupby(['atividade_tru68_ibge'])['Valor da produção'].sum().reset_index()

    	#2) agrupar Valor adicionado, emissões e credito
    	co2e_67_ = co2e_67.copy()
    	co2e_67_ = co2e_67_.rename(columns={'year': 'ano'})
    	co2e_67_t = co2e_67_[co2e_67_['ano']==int(self.sys.Y)]
    	scr_67_t = scr_67[scr_67['ano']==int(self.sys.Y)][['atividade_tru68_ibge','sum_carteira_ativa']]
    	scr_co2e_67 = vPBP_t_group.merge(co2e_67_t, on=['atividade_tru68_ibge'], how='left')
    	scr_co2e_67 = scr_co2e_67.merge(scr_67_t, on=['atividade_tru68_ibge'], how='left')
    	self.scr_co2e_67 = scr_co2e_67

    def coefficients(self):   	
    	#direct emission coefficients
    	coef67 = self.scr_co2e_67.copy()
    	if self.lulucf == True:
    	  coef67['q_direct'] = coef67['total_Gg_CO2e_GWP_SAR'] / coef67['Valor da produção']
    	else:
    	  coef67['q_direct'] = ( coef67['total_Gg_CO2e_GWP_SAR'] -  coef67['lulucf_Gg_CO2e_GWP_SAR'] ) / coef67['Valor da produção']

    	#total emission coefficients
    	coef67['q_total'] = self.mLeontiefBarr @ coef67['q_direct']#.values

    	#indirect emission coefficients
    	coef67['q_indirect'] = coef67['q_total'] - coef67['q_direct']

    	coef67.index = atividades_tru67	
    	self.coef67 = coef67

        

atividades_tru67 = ['0191\nAgricultura, inclusive o apoio à agricultura e a pós-colheita',
       '0192\nPecuária, inclusive o apoio à pecuária',
       '0280\nProdução florestal; pesca e aquicultura',
       '0580\nExtração de carvão mineral e de minerais não-metálicos',
       '0680\nExtração de petróleo e gás, inclusive as atividades de apoio',
       '0791\nExtração de minério de ferro, inclusive beneficiamentos e a aglomeração',
       '0792\nExtração de minerais metálicos não-ferrosos, inclusive beneficiamentos',
       '1091\nAbate e produtos de carne, inclusive os produtos do laticínio e da pesca',
       '1092\nFabricação e refino de açúcar',
       '1093\nOutros produtos alimentares', '1100\nFabricação de bebidas',
       '1200\nFabricação de produtos do fumo',
       '1300\nFabricação de produtos têxteis',
       '1400\nConfecção de artefatos do vestuário e acessórios',
       '1500\nFabricação de calçados e de artefatos de couro',
       '1600\nFabricação de produtos da madeira',
       '1700\nFabricação de celulose, papel e produtos de papel',
       '1800\nImpressão e reprodução de gravações',
       '1991\nRefino de petróleo e coquerias',
       '1992\nFabricação de biocombustíveis',
       '2091\nFabricação de químicos orgânicos e inorgânicos, resinas e elastômeros',
       '2092\nFabricação de defensivos, desinfestantes, tintas e químicos diversos',
       '2093\nFabricação de produtos de limpeza, cosméticos/perfumaria e higiene pessoal',
       '2100\nFabricação de produtos farmoquímicos e farmacêuticos',
       '2200\nFabricação de produtos de borracha e de material plástico',
       '2300\nFabricação de produtos de minerais não-metálicos',
       '2491\nProdução de ferro-gusa/ferroligas, siderurgia e tubos de aço sem costura',
       '2492\nMetalurgia de metais não-ferrosos e a fundição de metais',
       '2500\nFabricação de produtos de metal, exceto máquinas e equipamentos',
       '2600\nFabricação de equipamentos de informática, produtos eletrônicos e ópticos',
       '2700\nFabricação de máquinas e equipamentos elétricos',
       '2800\nFabricação de máquinas e equipamentos mecânicos',
       '2991\nFabricação de automóveis, caminhões e ônibus, exceto peças',
       '2992\nFabricação de peças e acessórios para veículos automotores',
       '3000\nFabricação de outros equipamentos de transporte, exceto veículos automotores',
       '3180\nFabricação de móveis e de produtos de indústrias diversas',
       '3300\nManutenção, reparação e instalação de máquinas e equipamentos',
       '3500\nEnergia elétrica, gás natural e outras utilidades',
       '3680\nÁgua, esgoto e gestão de resíduos', '4180\nConstrução',
       '4500\nComércio e reparação de veículos automotores e motocicletas',
       '4680\nComércio por atacado e a varejo, exceto veículos automotores',
       '4900\nTransporte terrestre', '5000\nTransporte aquaviário',
       '5100\nTransporte aéreo',
       '5280\nArmazenamento, atividades auxiliares dos transportes e correio',
       '5500\nAlojamento', '5600\nAlimentação',
       '5800\nEdição e edição integrada à impressão',
       '5980\nAtividades de televisão, rádio, cinema e  gravação/edição de som e imagem',
       '6100\nTelecomunicações',
       '6280\nDesenvolvimento de sistemas e outros serviços de informação',
       '6480\nIntermediação financeira, seguros e previdência complementar',
       '6800\nAtividades imobiliárias',
       '6980\nAtividades jurídicas, contábeis, consultoria e sedes de empresas ',
       '7180\nServiços de arquitetura, engenharia, testes/análises técnicas e P & D',
       '7380\nOutras atividades profissionais, científicas e técnicas',
       '7700\nAluguéis não-imobiliários e gestão de ativos de propriedade intelectual',
       '7880\nOutras atividades administrativas e serviços complementares',
       '8000\nAtividades de vigilância, segurança e investigação',
       '8400\nAdministração pública, defesa e seguridade social',
       '8591 + 8592\nEducação',
       '8691 + 8692\nSaúde',
       '9080\nAtividades artísticas, criativas e de espetáculos',
       '9480\nOrganizações associativas e outros serviços pessoais',
       '9700\nServiços domésticos','\nRESIDENCIAL']

        

def read(sector='agropecuaria',gas='CO2'):
  #File Path
  file_path = '/content/drive/MyDrive/projetos/Bacen/variaveis_ambientais/dicionario/dados_GHG_MCTI/sexta_edicao/estim_6a_ed_1990-2020_'
  #number of subsector
  if sector == "agropecuaria":
    n = 78
  elif sector == "energia":
    n = 32
  elif sector == "ippu":
    n = 28
  elif sector == "lulucf":
    n = 8
  elif sector == "residuos":
    n = 10
  elif sector == "total-brasil-1":
    n = 7
  else:
    n = None

  #select sheet
  #'CO2e_GWP_SAR'
  #'CO2e_GWP_AR5'
  #'CO2e_GTP_AR5'
  #'CO2'
  #'CH4'
  #'N2O'
  with resources.open_binary('sirene.MCTI.sexta_edicao', 'estim_6a_ed_1990-2020_'+sector+'.xlsx') as f:
    data = f.read()
    bytes_io = io.BytesIO(data)
  df = pd.read_excel(bytes_io, sheet_name=gas)
  df = df.loc[4:4+n,:]
  #set columns names
  new_columns = df.iloc[0]
  df = df[1:]
  df.columns = new_columns
  df.set_index(df.columns[0], inplace=True)
  df.rename_axis("setor_nfr", inplace=True)
  return df


