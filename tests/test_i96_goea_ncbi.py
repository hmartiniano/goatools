#!/usr/bin/env python

import os
from goatools.base import get_godag
from goatools.associations import get_assoc_ncbi_taxids
from goatools.go_enrichment import GOEnrichmentStudy
from goatools.test_data.genes_NCBI_9606_All import GeneID2nt


def test_i96():
    """Test to re-produce issue#96."""
    # Get genes
    study_ids = _get_geneids()
    population_ids = GeneID2nt.keys()
    # Get databases
    gene2go = get_assoc_ncbi_taxids([9606], loading_bar=None)
    fin_obo = os.path.join(os.getcwd(), "go-basic.obo")
    godag = get_godag(fin_obo, loading_bar=None)
    goeaobj = GOEnrichmentStudy(population_ids, gene2go, godag, methods=['fdr_bh'])
    # Run GOEA Gene Ontology Enrichment Analysis
    results_goeas = goeaobj.run_study(study_ids)


def _get_geneids():
    """Return study gene set."""
    symbol2geneid = {nt.Symbol:g for g, nt in GeneID2nt.items()}
    symbols = ['MICAL2', 'MIR1231', 'ZMIZ1', 'CRIM1', 'SMAD3', 'EFEMP1', 'CRIM1', 'ANXA2', 'VGLL3', 'FHL2', 'FSTL1', 'KIAA1456', 'MIR4316', 'MYH9', 'SIPA1L1', 'C15orf53', 'TRAM2', 'IGFBP7-AS1', 'CALD1',
    'RP5-1120P11.1', 'WNT2B', 'DDAH1', 'MIR1203', 'NRG1', 'SEC24D', 'NHSL2', 'ERGIC1', 'RPL37A', 'PTPN14', 'FEZ2', 'VEGFC', 'C2orf61', 'MIR30A', 'CAPZB', 'SMAD3', 'AAGAB', 'EPS8', 'ITGB5', 'LRP1-AS',
    'NRP1', 'WWTR1-AS1', 'CDK6', 'ENTPD6', 'THBS1', 'AC016735.2', 'ZCCHC24', 'LINC00592', 'HSPG2', 'MIRLET7A2', 'SMAD6', 'STARD13', 'EMP1', 'LINC00656', 'CALD1', 'C10orf142', 'ARID5B', 'MIR6809',
    'MIR5191', 'SNORA59A', 'KIAA1462', 'FERMT2', 'ADAMTS6', 'RBMS1', 'MIR8073', 'MBNL1-AS1', 'TGFBR1', 'SH2D4A', 'DST', 'OTX2-AS1', 'LAMA4', 'ASAP1', 'RP11-161M6.2', 'DST', 'SMAD7', 'AFAP1-AS1',
    'MIR4803', 'RP5-1158E12.3', 'LPCAT2', 'NDST1', 'FAM105A', 'SMURF2', 'RP4-673D20.3', 'ZMIZ1', 'NLRP1', 'NAV2-AS5', 'CCNL1', 'MICAL2', 'SH3RF1', 'IL1R2', 'LINC00161', 'MIR1294', 'MYLK-AS2', 'THBS1',
    'RNF24', 'TNS4', 'FBN1', 'DCUN1D3', 'CREB3L2', 'RSRP1', 'RP1-63G5.7', 'LINC01365', 'RPL23AP87', 'SNORA59A', 'DUSP7', 'TMEM163', 'EXT1', 'ATXN10', 'MIR4316', 'MYL9', 'ABHD2', 'ADCY5', 'LRTM2',
    'FAM83C', 'DLC1', 'LINC01057', 'SMAD6', 'NAV1', 'MIR584', 'TMEM212', 'COL15A1', 'PLCXD2', 'PRRX1', 'BCL10', 'MIR2278', 'FEM1B', 'ABTB2', 'NIPAL2', 'CDCP1', 'CCDC80', 'FBN1', 'DEFB104A', 'RP11-30P6.6',
    'LINC01085', 'AKAP2', 'ADAMTS20', 'MIR3152', 'LMO7-AS1', 'RP11-887P2.5', 'ARHGAP26-IT1', 'TSPAN17', 'CYP3A43', 'CORO2B', 'RP3-332B22.1', 'RARA', 'MSN', 'UMODL1', 'C12orf74', 'TRAM2', 'LHFPL2',
    'TRIP13', 'PALLD', 'NRP2', 'LINC00607', 'COL6A3', 'CLMP', 'MIR4316', 'PTPN14', 'LINC01354', 'CBR4', 'FNDC3B', 'LINC01426', 'WISP2', 'NUDT6', 'MIR6083', 'GRHL1', 'KIF13A', 'VCL', 'MIR125B1',
    'FOXP1-AS1', 'CLCF1', 'CDK5RAP2', 'RP11-356I2.4', 'NEK6', 'CTLA4', 'SLC8A1-AS1', 'BACH1', 'MIR100', 'MIR3619', 'CD44', 'GOLT1A', 'LUM', 'BCAS3', 'MIR1208', 'NGF', 'INHBA', 'MRPS23', 'STK40', 'HK1',
    'ASAP2', 'WBP1L', 'HMCN2', 'DEFB104B', 'VAC14', 'MYOF', 'PTGIS', 'KIRREL', 'MAP4K4', 'GALNT10', 'LHFPL3-AS2', 'EGFR', 'TGM2', 'DMRTB1', 'YPEL5', 'EPG5', 'FNDC3B', 'SND1', 'MIR6827', 'MIR3126',
    'LAMA4', 'PPIF', 'ITGB1', 'SEMA5B', 'TEAD1', 'PAMR1', 'GCLM', 'NFIB', 'TM4SF4', 'LINC01132', 'BASP1', 'SPECC1', 'MAPKAPK2', 'CSRP1', 'NID2', 'DST', 'ERG', 'GLI2', 'TMEM50A', 'MIR29A', 'NBPF26',
    'LRRC8D', 'LINC01119', 'FNDC3B', 'LINC00917', 'GADD45A', 'SP3', 'LINC01625', 'ADAMTS9-AS1', 'TCF23', 'NPLOC4', 'MIR1252', 'ZEB2-AS1', 'NEURL1-AS1', 'SLC25A51', 'XPNPEP1', 'WASF2', 'SLC25A3P1',
    'GPR88', 'RXFP2', 'RUNX1T1', 'ME3', 'RAI14', 'PNMA2', 'TOM1L2', 'CWC22', 'R3HCC1', 'MYLK-AS2', 'ERVFRD-1', 'FENDRR', 'TIPARP', 'SMAD6', 'TPM1', 'RP11-266L9.4', 'B4GALT1', 'REP15', 'MIR8052', 'LAMB1',
    'FRMD6-AS1', 'ETS1', 'COL1A2', 'MIR4289', 'MAP1B', 'NABP1', 'SLC8A1-AS1', 'NOTCH2', 'ZMIZ1', 'GRHL2', 'CTD-2015G9.1', 'DLC1', 'CCNL1', 'NBPF14', 'ITGA11', 'TNS3', 'TTPAL', 'NBPF19', 'STAT3',
    'MIR4668', 'LINC00607', 'CARMN', 'COL22A1', 'MIR583', 'WT1', 'NEK7', 'PLEKHG4B', 'TIGD6', 'RP11-778O17.4', 'NOTCH2', 'SPACA1', 'TEAD1', 'TOX2', 'GALNT2', 'EVX2', 'SALRNA3', 'DEFB103B', 'CCDC12',
    'ITGAE', 'EXT1', 'RRBP1', 'TMEM189-UBE2V1', 'SEPT11', 'EXT1', 'ZBTB38', 'ASTN2-AS1', 'RAI1', 'LETM2', 'HIPK2', 'CLMP', 'PDLIM5', 'UBR5', 'RP1-102K2.8', 'RREB1', 'MIR1260B', 'NEK6', 'ARHGEF12',
    'PRR16', 'STRA6', 'MIR222', 'SH3RF1', 'STK35', 'RDH10-AS1', 'RP5-1070A16.1', 'AP3M1', 'ANKRD33B', 'SNORA3B', 'ANKRD40', 'PRRC2B', 'LAMC1', 'ADAMTSL1', 'EDN2', 'FMN1', 'CACNA1C-AS4', 'RP11-90C4.2',
    'MBNL1-AS1', 'TARS', 'LIPC', 'ASAP1', 'MIR6090', 'PAX2', 'CHD2', 'DLC1', 'LPCAT1', 'CITF22-92A6.2', 'NAV1', 'HIPK2', 'CCNI', 'C6orf89', 'VAC14-AS1', 'LINC01225', 'TRIM8', 'ADAM12', 'LMCD1',
    'RP11-205K6.1', 'PPFIBP1', 'SLC4A4', 'TBX15', 'ACOXL', 'FAM83C', 'DYRK1A', 'AC109344.1', 'DUSP1', 'RPL22L1', 'NCOA4', 'LOXL1-AS1', 'CORO1C', 'CMSS1', 'CYP11A1', 'SYNJ2-IT1', 'EPS8L3', 'RP11-366L20.2',
    'RP4-569M23.5', 'PAX8', 'MIR3152', 'ACKR3', 'LTBP2', 'ARSJ', 'RFTN1', 'FHL1', 'NARS2', 'EXT1', 'SH3BGRL3', 'ADAMTS2', 'COL8A1', 'IRF2BPL', 'NREP', 'NOTCH2NL', 'USP2', 'HSPH1', 'SKOR2', 'C16orf72',
    'ENPP2', 'TSPAN18', 'IRF1', 'TNC', 'OPTC', 'PDLIM5', 'PGBD3', 'CCDC167', 'COL12A1', 'RIMBP3', 'TFPI', 'SOCS5', 'HSPG2', 'SH2B3', 'LINC00316', 'DDR2', 'BCL10', 'LINC01132', 'ABHD5', 'TGFB3', 'DYSF',
    'TRPA1', 'TRIM8', 'UCK2', 'SOST', 'COL5A2', 'CA4', 'IGDCC3', 'SIPA1L1', 'SRCIN1', 'AP001626.1', 'AC010091.1', 'RAI1-AS1', 'MIR1260B', 'TCHP', 'RP11-168P8.5', 'BDKRB1', 'TSPYL5', 'MYLK-AS2', 'FOSL2',
    'MIR4743', 'TGFBI', 'AC020571.3', 'THBS1', 'NANOS1', 'LINC01447', 'LMO7-AS1', 'AP2S1', 'RMDN2', 'MIR4316', 'DCLK2', 'MIR4280', 'NFATC3', 'SEMA5B', 'MYO1B', 'ROR1', 'MED15', 'NFX1', 'HIC1', 'MIR1203',
    'STX1A', 'ANKFN1', 'CTB-113D17.1', 'MIR205HG', 'FAM129B', 'SH3BP4', 'RP11-478P10.1', 'MIR151A', 'CACNG4', 'CRYBA1', 'APBB2', 'CCDC80', 'TRIO', 'F2R', 'RAF1', 'CYTOR', 'ITGB6', 'PITPNB', 'DHRS3',
    'WDFY2', 'RNF141', 'ARL6IP5', 'MIR4435-2', 'MAP4K4', 'MIRLET7I', 'RND3', 'CXXC5', 'SNORA70E', 'ANXA2', 'KCCAT211', 'PLCB1', 'TMCC2', 'EXT1', 'RP11-366L20.2', 'WDR86-AS1', 'HMG20A', 'RP11-38F22.1',
    'FYCO1', 'LPP', 'HABP2', 'TSPEAR', 'ABLIM1', 'RP11-443B7.1', 'FAM20B', 'RASSF10', 'XPC', 'TNIP3', 'ACSL4', 'MTMR2', 'TNIK', 'RELT', 'CRIPT', 'RP11-572C15.5', 'CCDC81', 'CMSS1', 'C6orf223', 'SHISA4',
    'PDGFA', 'HS1BP3-IT1', 'MYPN', 'XCR1', 'ZFP36L1', 'CBR4', 'TRAPPC3', 'MIR802', 'CSRP1', 'DAPK2', 'SPESP1', 'RP11-890B15.3', 'SHB', 'INSIG2', 'ADGRG1', 'GPC6-AS1', 'KIRREL3-AS3', 'LXN', 'CBR4', 'CPA1',
    'MINPP1', 'NFIX', 'FLRT2', 'MIR6070', 'USP3', 'PRR16', 'ALPL', 'RP11-379K22.2', 'ADAMTSL1', 'RRBP1', 'RP11-430H10.2', 'MAPKAPK3', 'ABHD16B', 'CDKN3', 'STEAP3-AS1', 'RTP3', 'SLA', 'CYP1B1-AS1',
    'MIR6888', 'HIVEP3', 'LINC01119', 'CCDC71L', 'MACF1', 'EFNB1', 'CBLB', 'MIR760', 'NAMA', 'LNX1-AS1', 'KMT2E', 'PYROXD2', 'LMO7DN', 'EML4', 'CCDC80', 'SEC22A', 'COL21A1', 'CDC42EP3', 'EPHA2', 'CAPZA2',
    'PHLDB2', 'TPPP', 'MIR3129', 'LIMA1', 'PDE1C', 'RUNX2', 'SPRED2', 'C1QTNF1', 'EPHA2', 'IRF1', 'MIR4263', 'RXFP2', 'MTNR1A', 'CUEDC1', 'GCNT1', 'MIR3152', 'ST5', 'ITGA11', 'RP11-366L20.2', 'MAGI2',
    'KCCAT211', 'MIR6090', 'EMX1', 'CDC42EP3', 'PKP4', 'BCL10', 'SERPINB7', 'IKBKE', 'AGMO', 'RUNX1', 'PHC2', 'SH2D7', 'PARVA', 'B4GALT5', 'STAT4', 'ACTN4', 'RTKN2', 'MIR1260B', 'SH3PXD2B', 'ACTN1-AS1',
    'LINC00882', 'SLC8A1', 'NREP-AS1', 'THADA', 'DDAH1', 'MIR4274', 'SERPINE1', 'ASAP1-IT2', 'APH1B', 'IGF2BP2-AS1', 'MUSK', 'TRAF3IP2', 'COLEC12', 'EXT1', 'FLJ22447', 'CTB-113P19.1', 'RBPJ',
    'RP11-230G5.2', 'PALLD', 'SLC1A2', 'MIR190A', 'FHOD3', 'LHFPL2', 'C2CD5', 'SLCO4A1', 'SYPL1', 'ARHGAP18', 'MIR4703', 'SOX1', 'DIXDC1', 'TM2D3', 'MIR4743', 'CASC23', 'KDM4C', 'RAI14', 'MYOZ3',
    'MAP3K12', 'MIR2278', 'HPCAL1', 'C2orf78', 'DNASE2B', 'RP1-111D6.4', 'AC007246.3', 'SRGAP2B', 'CTD-2078B5.2', 'RMI2', 'PDGFC', 'PSAP', 'KLF4', 'MYO1B', 'PDGFC', 'EPHA2', 'MGC27382', 'FAM188B', 'FLNB',
    'ATP2B4', 'NR3C1', 'DUOX1', 'UPF1', 'MIR802', 'DLD', 'EDN2', 'ZNF703', 'IRAK1', 'ASB6', 'FENDRR', 'FAM105A', 'NAV2-AS5', 'SMG9', 'ELL', 'TNFRSF11B', 'LINC00619', 'LAMC1', 'MYLK', 'FAAP100', 'MIR8052',
    'ACSL4', 'ANK3', 'COL5A1-AS1', 'PXN', 'TSPAN18', 'PCSK1', 'TOR3A', 'COPS8', 'RRAS2', 'ERRFI1', 'CDH2', 'TMOD3', 'NFIB', 'AFAP1', 'SMIM14', 'PTRH2', 'EIF2D', 'PTPN1', 'MIR8079', 'NRP1', 'TCF21',
    'IL1R1', 'FAP', 'TNS3', 'COBL', 'PDLIM5', 'RAD51B', 'C9orf152', 'RFLNA', 'SYT2', 'LINC01101', 'DLX4', 'ZMIZ1', 'PLCE1-AS2', 'JPH3', 'SEC61A1', 'AC007163.3', 'NKX3-2', 'COL8A1', 'LINC01151', 'DERA',
    'Z99756.1', 'CEL', 'GYG1', 'MIR551A', 'TNKS1BP1', 'FAM20A', 'RPTN', 'NSMAF', 'DEFB103A', 'MIR3937', 'BRD4', 'MIR4256', 'DTWD1', 'DDX25', 'SMYD2', 'ADAMTS8', 'ITGA3', 'ZNF705B', 'SLC35F4', 'LINC00656',
    'RASA4', 'ADAMTS2', 'KCNK3', 'MYEOV', 'SKI', 'CAMK2D', 'NAA20', 'ITGA3', 'RP5-1172A22.1', 'NEK7', 'CASZ1', 'LINC00882', 'DPP4', 'CTD-2193G5.1', 'HEPHL1', 'SEMA5B', 'SLC6A9', 'ADM', 'LUCAT1',
    'RP11-284G10.1', 'RP11-177H13.2', 'SPECC1L', 'EXT1', 'PTX3', 'LUZP4', 'SLC6A6', 'RAP1B', 'FBN1', 'AKAP2', 'MPRIP', 'CFDP1', 'CTB-113P19.1', 'NRG2', 'KBTBD12', 'PPARD', 'SH3BP4', 'STK24', 'MIR4725',
    'TEAD1', 'LINC01118', 'EPSTI1', 'PVT1', 'CUZD1', 'IGFBP7-AS1', 'SLC7A1', 'AC013461.1', 'BCL2L14', 'IGFBP5', 'MIR620', 'NRG1-IT3', 'BRD4', 'ADAM19', 'ATP6V0D1', 'NFIX', 'PCA3', 'ACTL8', 'TGM4',
    'MIR1-1', 'CORO2B', 'SH3PXD2B', 'PLXNA1', 'EPS8L3', 'LAMB1', 'SLC22A23', 'ALX4', 'EHD4', 'DUSP6', 'FRMD6-AS2', 'ENTPD7', 'SIPA1L1', 'SH3PXD2A-AS1', 'TUBB2B', 'SNORA72', 'MIR1293', 'TRIL', 'GDF6',
    'FAT1', 'ARHGAP35', 'HTRA1', 'IGFL3', 'NTM', 'H1F0', 'EBF2', 'CCL2', 'SGIP1', 'TGFBI', 'MED9', 'SNTB1', 'SCRT1', 'AMPD3', 'COL6A3', 'RARRES1', 'FERMT2', 'CEBPG', 'SOCS5', 'RMDN2', 'DENND5B', 'PDZD4',
    'MIR8056', 'TARID', 'MAGI1-AS1', 'SYNPO2', 'ARNT2', 'KDM5C', 'HSD52', 'ZDHHC13', 'C9orf152', 'MED30', 'SBF2-AS1', 'CTD-2078B5.2', 'CAPZB', 'SHISA8', 'MIR1262', 'HOPX', 'PRDM12', 'SEMA3D',
    'RP5-1142A6.8', 'MAPKAPK2', 'PDE4B', 'LINC00882', 'NBPF14', 'DLEU1-AS1', 'NR5A1', 'MIR6720', 'ADAM12', 'ADAM30', 'RAPGEF4', 'AC006262.6', 'RGS3', 'SMAD6', 'SYNJ2-IT1', 'TEX2', 'LINC00381', 'DST',
    'MPZL1', 'BNC2', 'MIR4674', 'ARFGAP3', 'ADRA1D', 'SLIT3', 'COL27A1', 'SLC25A51', 'ATG16L2', 'ZMIZ1', 'MIR129-1', 'MTDH', 'MIR7848', 'MIR4430', 'HOXC13', 'PARD3', 'CAMK2B', 'ABHD5', 'RPLP1', 'MPEG1',
    'MLK7-AS1', 'QKI', 'SMYD2', 'ZBTB17', 'C6orf222', 'NAV2-AS5', 'OVAAL', 'LINC01048', 'TNFSF8', 'DHRS12', 'MACF1', 'PLEKHA2', 'LINC00926', 'EHF', 'KCNJ6', 'MYO1B', 'MIR2278', 'WASL', 'SRP9',
    'MIR4520-1', 'LINC01500', 'SLC30A2', 'PRPH2', 'RP11-221J22.1', 'SNORA31', 'SIPA1L1', 'SERAC1', 'EGFR', 'SLC38A2', 'FRMPD3', 'RP11-430H10.2', 'NUAK2', 'CELF1', 'CD36', 'CHSY1', 'ERGIC1', 'ZNF488',
    'SEMA6B', 'CISTR', 'MFNG', 'HS1BP3-IT1', 'NBPF10', 'CYTOR', 'CPED1', 'MIR378G', 'BMPER', 'ARFGAP3', 'RAB8B', 'LINC00917', 'ABCA17P', 'FHL2', 'MIR620', 'SPRED2', 'RAI14', 'ZSCAN20', 'MMD', 'MIR548Q',
    'SNORA3B', 'MIR7854', 'CEP350', 'RGAG4', 'HRCT1', 'CCL8', 'IL24', 'TBC1D4', 'IRS1', 'SLC8A1', 'PLS3-AS1', 'SIL1', 'LMO2', 'FGF3', 'RNVU1-19', 'LEPROT', 'MIR4774', 'CREB3L2', 'TSPAN2', 'KCNIP3',
    'MAP3K14', 'RASSF8', 'MIR4419A', 'EFHC1', 'MIR297', 'KSR1', 'GSN', 'ATG4A', 'VASN', 'BBS12', 'NUFIP1', 'CAMK2D', 'PPL', 'H2AFY', 'CRTAM', 'RP11-47I22.2', 'BLID', 'HTR2B', 'GPR183', 'UQCC2', 'WDR36',
    'ACTL8', 'COLEC12', 'CCDC85B', 'LINC00607', 'ITGA11', 'MBNL1-AS1', 'KRT85', 'LINC01478', 'LTBP2', 'NRG1', 'ALX4', 'ITGA11', 'MBOAT2', 'HELT', 'ZFP36L1', 'CISTR', 'FAM76B', 'CISTR', 'CDK5RAP2',
    'TINAGL1', 'SNORD96B', 'RP11-1008C21.1', 'CMSS1', 'RP11-367G18.1', 'MRPL33', 'AC012462.2', 'ZMIZ1', 'TSPAN18', 'PANDAR', 'MIR6888', 'MIR548AH', 'RP11-162I7.1', 'MIR548AZ', 'ABHD5', 'GALNT5', 'ANKRD1',
    'RP11-554D15.1', 'CALD1', 'CAV1', 'OLFML2B', 'RP11-363D14.1', 'RP11-443B7.1', 'MIR629', 'ASB1', 'GFRA1', 'CHAMP1', 'MIR2052', 'ADAMTSL4', 'NAIF1', 'MIR190A', 'THSD4', 'KCNIP3', 'TIAF1', 'MIR4265',
    'RP11-245G13.2', 'PYGL', 'OXCT1-AS1', 'GLI2', 'CDC42EP3', 'PLAU', 'CLIC4', 'ERMN', 'USP12', 'PLXNB2', 'WARS', 'SNORA72', 'LATS2', 'PLXNA4', 'RP5-898J17.1', 'PSD3', 'CTSC', 'TBX20', 'GDNF', 'TOP1',
    'DOK1', 'GPR12', 'LINC01082', 'MIR7973-1', 'MIR548AJ1', 'PPP1R3C', 'NPIPB11', 'MLXIP', 'RP11-890B15.3', 'RASA4B', 'MIR619', 'NFATC4', 'ABRA', 'CHML', 'SYNDIG1', 'PEAR1', 'LIFR-AS1', 'HIF1AN',
    'FOXP1-AS1', 'SELPLG', 'EFCAB1', 'MIR4743', 'WBSCR28', 'NHS-AS1', 'ABCA1', 'SOGA1', 'ARID5B', 'BICC1', 'CRY2', 'RASD2', 'MINOS1', 'MIR4277', 'PLAC9', 'MYLK-AS2', 'TCF21', 'WIPF1', 'MYF6',
    'AC007880.1', 'LINC00189', 'FST', 'TBC1D2', 'IL34', 'MIR101-2', 'NRG1-IT3', 'APOA1', 'CAV2', 'MIR4642', 'ATP8B1', 'ATG16L2', 'PDGFRL', 'MYO1B', 'TIMP3', 'CD82', 'MIR4319', 'ANKEF1', 'NPFFR1', 'ZHX2',
    'SHQ1', 'NGF', 'AC002480.2', 'LINC01592', 'SRGAP2', 'RP11-148B18.1', 'LOXL1-AS1', 'KIF6', 'GGTA1P', 'ROS1', 'GNB1L', 'THY1', 'SIX6', 'ABL1', 'AC002480.3', 'SFTPB', 'KSR1', 'FMNL1', 'ARHGEF16',
    'CREB5', 'NPC1', 'MIR760', 'ADAMTS20', 'DAPL1', 'SLC22A12', 'LINC01276', 'SLC22A5', 'EML4', 'TPST1', 'FLJ45079', 'ARRB1', 'CCDC34', 'NEK7', 'AQP9', 'BBOX1-AS1', 'ASAP1-IT2', 'WDR61', 'CTA-929C8.6',
    'LFNG', 'FAM188B', 'CALD1', 'ZFAND3', 'GTF3A', 'CYP26B1', 'KIF3A', 'MIR1252', 'MIR4424', 'MYO1B', 'SVIL', 'REV1', 'YWHAH', 'TSPAN14', 'PNMA1', 'RP11-111I12.1', 'CTGF', 'PDGFRA', 'CRISPLD2', 'HAND2',
    'RP11-1124B17.1', 'SLC4A4', 'TMEM75', 'NABP1', 'RUSC2', 'PDGFC', 'MIR4476', 'ARHGEF10L', 'PIK3R1', 'RARB', 'C14orf132', 'PDGFC', 'GFRA2', 'MIR4711', 'XYLT1', 'PLOD2', 'DIEXF', 'VEGFC', 'CTTN',
    'ZNF618', 'MIR3937', 'MED15', 'NRP2', 'AC064834.3', 'FOXS1', 'AQP1', 'UTRN', 'MRPL33', 'CMTM4', 'AKR1C1', 'ALX4', 'TMEM241', 'SAMD12', 'FST', 'TFAP2A', 'MATN1-AS1', 'LINC00484', 'KIF12', 'PHLDA3',
    'C8orf86', 'LINC01143', 'AFAP1-AS1', 'FNBP1L', 'SPAG6', 'RIPK2', 'KY', 'VSX1', 'SACM1L', 'CYTOR', 'STK17B', 'MAPRE1', 'TLDC1', 'PLXND1', 'GUSBP5', 'MIR4293', 'DCAF5', 'DOCK1', 'PRRX1', 'CRAT40',
    'AL450226.2', 'CISH', 'RP11-137H2.4', 'BIN1', 'LINC00837', 'CCNYL1', 'UBE2H', 'LIFR-AS1', 'CCDC171', 'CACNG4', 'ZBTB40', 'ANXA2', 'MYRIP', 'EVC', 'DCPS', 'ZBTB38', 'RTN4', 'S100A11', 'PSMB7', 'SP6',
    'TSPEAR', 'INSC', 'FLJ42102', 'MIR1205', 'ISLR']
    geneids = [symbol2geneid[symbol] for symbol in symbols if symbol in symbol2geneid]
    print("{N} study Symbols".format(N=len(symbols)))
    print("{N} study GeneIDs".format(N=len(geneids)))
    return geneids


if __name__ == '__main__':
    test_i96()
