import os
import decimal
file_name= input ('Please enter the file name ')
file1 = open(file_name)
file2 = open("modified.pdb","w")
line1=[]
for line in file1:

    if line.startswith(("ATOM" or "HETATM" or "ANISOU" )):
        atomType = line[0:6]
        atomSerialNumber = line[6:11]
        atomName = line[12:16]
        resName = line[16:20]
        chain = line[21]
        resNumber = line[22:26]
        coorX = line[30:38]
        coorY = line[38:46]
        coorZ = line[46:54]
        occupancy = line[54:60]
        temperatureFact = line[60:66]
        segmentIdentifier = line[72:76]
        elementSymbol = line[76:78]
        if float(occupancy) < 1.00 and float(occupancy) != 1.00:
            if not resName.startswith("A"):
                occupancy = str('0.30')
                # the below hard coded formatting is required to retain the PDB file format
                #line1 =atomType+atomSerialNumber+' '+atomName+resName+' '+ chain+resNumber+'     '+coorX+coorY+coorZ+'   '+occupancy+temperatureFact+segmentIdentifier+'    '+elementSymbol+'\n'

                # in here the logic is the occupancy of all alt confs (B, C etc) are already set to zero
                line1= line.replace("0.00","0.30")
                file2.write(line1)
                #print(str(line1))
            else:
                file2.write(line)
        else:
            file2.write(line)
    else:
        file2.write(line)

file1.close()