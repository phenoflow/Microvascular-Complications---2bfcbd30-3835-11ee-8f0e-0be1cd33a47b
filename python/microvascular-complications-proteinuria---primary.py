# Evangelos Kontopantelis, David A Springate, David Reeves, Darren M. Aschroff, Martin Rutter, Iain Buchan, Tim Doran, Matthias Pierce, Darren M. Ashcroft, 2023.

import sys, csv, re

codes = [{"code":"1Z1H.00","system":"readv2"},{"code":"1Z1H.11","system":"readv2"},{"code":"1Z1J.00","system":"readv2"},{"code":"1Z1J.11","system":"readv2"},{"code":"1Z1K.00","system":"readv2"},{"code":"1Z1K.11","system":"readv2"},{"code":"1Z1L.00","system":"readv2"},{"code":"1Z1L.11","system":"readv2"},{"code":"K08yA00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('microvascular-complications-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["microvascular-complications-proteinuria---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["microvascular-complications-proteinuria---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["microvascular-complications-proteinuria---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
