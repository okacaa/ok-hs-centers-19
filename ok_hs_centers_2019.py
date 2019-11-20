import os
import numpy as np
import pandas as pd

df = pd.read_csv("https://eclkc.ohs.acf.hhs.gov/sites/default/files/locatordata/ALL_all.csv")

df.to_csv('inputs/ALL_all.csv')

df['programname'] = df.programDelegateName.replace('Big Five Community Services, Inc.',
                                                   'Big Five Community Services') \
.replace(['Cherokee Nation Early Childhood Unit',
          'Cherokee Nation Early Head Start'],
         'Cherokee Nation') \
.replace('CHEYENNE & ARAPAHO TRIBES OF OKLAHOMA',
         'Cheyenne & Arapaho Tribes of Oklahoma') \
.replace('CHOCTAW NATION OF OKLAHOMA EDUCATION DEPARTMENT',
         'Choctaw Nation of Oklahoma') \
.replace('Central Tribes of the Shawnee Area, Inc.',
         'Central Tribes of the Shawnee Area') \
.replace('CHEYENNE & ARAPAHO TRIBES OF OKLAHOMA',
         'Cheyenne & Arapaho Tribes of Oklahoma') \
.replace('CMTY ACTION AGCY OF OK CY & CTY & OK/CANADIAN CTYS INC',
         'CAA of OKC & OK/Canadian Counties') \
.replace(['Community Action Project of Tulsa County (CAP)',
          'Community Action Project of Tulsa County, Inc.'],
         'Community Action Project of Tulsa County') \
.replace('COMMUNITY ACTION RESOURCE AND DEVELOPMENT, INC.',
         'Community Action Resource and Development') \
.replace('Crossroads Youth & Family Services, Inc.',
         'Crossroads Youth & Family Services') \
.replace('Delta Community Action Foundation, Inc.',
         'Delta Community Action Foundation') \
.replace('Green Country Behavioral Health Services, Inc.',
         'Green Country Behavioral Health Services') \
.replace('INCA COMMUNITY SERVICES, INC',
         'INCA Community Services') \
.replace('IOWA TRIBE OF OKLAHOMA',
         'Iowa Tribe of Oklahoma') \
.replace('KI BOIS COMMUNITY ACTION FOUNDATION, INC',
         'KI BOIS Community Action Foundation') \
.replace('Kickapoo Head Start',
         'Kickapoo Tribe of Oklahoma') \
.replace('KIOWA TRIBE (ONAP)',
         'Kiowa Tribe') \
.replace(['LITTLE DIXIE COMMUNITY ACTION AGENCY, INC',
          'Little Dixie Community Action Agency, Inc.'],
         'Little Dixie Community Action Agency') \
.replace('Muscogee (Creek) Nation Head Start',
         'Muscogee (Creek) Nation') \
.replace('NATIVE AMERICAN COALITION OF TULSA',
         'Native American Coalition of Tulsa') \
.replace('Northeast Oklahoma Community Action Agency, Inc.',
         'Northeast Oklahoma Community Action Agency') \
.replace('OSAGE NATION',
         'Osage Nation') \
.replace('OTOE-MISSOURIA TRIBAL COUNCIL',
         'Otoe-Missouria Tribal Council') \
.replace('SEMINOLE NATION OF OKLAHOMA',
         'Seminole Nation of Oklahoma') \
.replace(['SOUTHWEST OK COMMUNITY ACTION GROUP, INC',
          'Southwest Oklahoma Community Action Group, Inc.'],
         'Southwest Oklahoma Community Action Group') \
.replace(['SUNBEAM FAMILY SERVICES INC',
          'SUNBEAM FAMILY SERVICES, INC',
          'SUNBEAM FAMILY SERVICES, INC.',
          'Sunbeam Family Services, Inc.'],
         'Sunbeam Family Services') \
.replace('The Chickasaw Nation Head Start',
         'The Chickasaw Nation') \
.replace('Tulsa Educare, Inc.',
         'Tulsa Educare') \
.replace('United Community Action Program, Inc.',
         'United Community Action Program') \
.replace('WASHITA VALLEY COMMUNITY ACTION COUNCIL, INC',
         'Washita Valley Community Action Council')

ok = df.loc[df['state'] == 'OK',['programname','county','name','address','city','state','zip','phone']]

ok['contact'] = ok[['address','city','state','zip','phone']].astype(str).apply(' '.join, axis=1)

dfin = ok.set_index(['programname', 'county'])

dfin.to_csv('outputs/ok_hs_centers_19.csv')
