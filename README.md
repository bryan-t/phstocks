# phstocks

Provides utility functions for gathering PH stock data which I use for learning/practicing machine learning.
Note that this is not published and needs to be manually built and installed.

### Getting Symbols

```
>>> from phstocks.gather.stocks import get_stock_symbols
>>> get_stock_symbols()
['2GO', '8990P', 'AAA', 'AB', 'ABA', 'ABG', 'ABS', 'ABSP', 'AC', 'ACE', 'ACEN', 'ACEX', 'ACPA', 'ACPB1', 'ACR', 'AEV', 'AGI', 'ALCO', 'ALCPB', 'ALCPC', 'ALHI', 'ALI', 'ALLHC', 'ANI', 'ANS', 'AP', 'APB2R', 'APC', 'APL', 'APO', 'APVI', 'APX', 'AR', 'ARA', 'AREIT', 'AT', 'ATI', 'ATN', 'ATNB', 'AUB', 'AXLM', 'BC', 'BCB', 'BCOR', 'BCP', 'BDO', 'BEL', 'BH', 'BHI', 'BKR', 'BLFI', 'BLOOM', 'BMM', 'BPI', 'BRN', 'BSC', 'C', 'CA', 'CAB', 'CAT', 'CDC', 'CEB', 'CEBCP', 'CEI', 'CEU', 'CHI', 'CHIB', 'CHP', 'CIC', 'CIP', 'CLI', 'CNPF', 'CNVRG', 'COAL', 'COL', 'COSCO', 'CPG', 'CPGP', 'CPM', 'CPV', 'CPVB', 'CROWN', 'CSB', 'CYBR', 'DAVIN', 'DD', 'DDMPR', 'DDPR', 'DELM', 'DFNN', 'DITO', 'DIZ', 'DMC', 'DMCP', 'DMPA1', 'DMPA2', 'DMW', 'DNA', 'DNL', 'DTEL', 'DWC', 'EAGLE', 'ECP', 'EEI', 'EG', 'ELI', 'EMP', 'EURO', 'EVER', 'EW', 'FAF', 'FB', 'FBP', 'FBP2', 'FDC', 'FERRO', 'FEU', 'FFI', 'FGEN', 'FGENG', 'FJP', 'FJPB', 'FLI', 'FMETF', 'FNI', 'FOOD', 'FPH', 'FPHPC', 'FPI', 'FRUIT', 'GEO', 'GERI', 'GLO', 'GLOPA', 'GLOPP', 'GMA7', 'GMAP', 'GPH', 'GREEN', 'GSMI', 'GTCAP', 'GTPPA', 'GTPPB', 'HI', 'HLCM', 'HOME', 'HOUSE', 'HVN', 'I', 'ICT', 'IDC', 'IMI', 'IMP', 'ION', 'IPM', 'IPO', 'IRC', 'IS', 'JAS', 'JFC', 'JGS', 'JOH', 'KEP', 'KPH', 'KPHB', 'KPPI', 'LAND', 'LBC', 'LC', 'LCB', 'LFM', 'LMG', 'LODE', 'LOTO', 'LPZ', 'LR', 'LRP', 'LRW', 'LSC', 'LTG', 'MA', 'MAB', 'MAC', 'MACAY', 'MAH', 'MAHB', 'MARC', 'MAXS', 'MB', 'MBC', 'MBT', 'MED', 'MEG', 'MER', 'MFC', 'MFIN', 'MG', 'MHC', 'MJC', 'MJIC', 'MM', 'MPI', 'MRC', 'MRSGI', 'MVC', 'MWC', 'MWIDE', 'MWP', 'NI', 'NIKL', 'NOW', 'NRCP', 'OM', 'OPM', 'OPMB', 'ORE', 'OV', 'PA', 'PAL', 'PAX', 'PBB', 'PBC', 'PCOR', 'PERC', 'PGOLD', 'PHA', 'PHES', 'PHN', 'PHR', 'PIZZA', 'PLC', 'PMPC', 'PNB', 'PNX', 'PNX3A', 'PNX3B', 'PNX4', 'PNXP', 'PORT', 'PPC', 'PRC', 'PRF2A', 'PRF2B', 'PRF3A', 'PRF3B', 'PRIM', 'PRMX', 'PSB', 'PSE', 'PTC', 'PX', 'PXP', 'RCB', 'RCI', 'REG', 'RFM', 'RLC', 'RLT', 'ROCK', 'ROX', 'RRHI', 'SBS', 'SCC', 'SECB', 'SEVN', 'SFI', 'SFIP', 'SGI', 'SGP', 'SHLPH', 'SHNG', 'SLF', 'SLI', 'SM', 'SMC', 'SMC2A', 'SMC2B', 'SMC2C', 'SMC2D', 'SMC2E', 'SMC2F', 'SMC2G', 'SMC2H', 'SMC2I', 'SMCP1', 'SMPH', 'SOC', 'SPC', 'SPM', 'SRDC', 'SSI', 'SSP', 'STI', 'STR', 'SUN', 'T', 'TBGI', 'TCB2A', 'TECH', 'TEL', 'TFC', 'TFHI', 'TUGS', 'UBP', 'UNI', 'UPM', 'URC', 'V', 'VITA', 'VLL', 'VMC', 'VUL', 'VVT', 'WEB', 'WIN', 'WLCON', 'WPI', 'X', 'ZHI']
```

### Getting Stock Data

```
>>> from phstocks.gather.stocks import get_stock_data
>>> get_stock_data('2GO', '03-25-2021', '03-29-2021');
fetching:  2GO 03-25-2021 03-29-2021
            open      value  close  high   low
dt
2021-03-25  8.46   762680.0   8.50   8.5  8.46
2021-03-26  8.50   621865.0   8.46   8.5  8.40
2021-03-29  8.40  2298308.0   8.50   8.6  8.40
```

## Getting Closing Price of All Stocks

```
>>> from phstocks.gather.stocks import get_all_stock_close
>>> get_all_stock_close('03-25-2021', '03-29-2021')
             2GO  AAA     AB   ABA  ABG    ABS   ABSP    AC  ...   VUL    VVT   WEB    WIN  WLCON   WPI     X    ZHI
dt                                                           ...
2021-03-25  8.50  NaN  11.00  1.21  7.1  11.00  10.38  6.96  ...  2.20  14.50  2.75  0.240  17.94  0.54  23.0  0.209
2021-03-26  8.46  NaN  11.06  1.13  7.2  11.06  10.40  6.99  ...  2.12  14.82  2.77  0.255  17.46  0.56  24.0  0.214
2021-03-29  8.50  NaN  11.50  1.12  7.2  11.50  10.94  6.93  ...  2.06  14.80  2.80  0.240  17.88  0.55  23.0  0.195 
```
