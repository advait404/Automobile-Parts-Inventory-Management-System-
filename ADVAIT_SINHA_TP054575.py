#Advait Sinha
#TP054575



def menu():
    #listing all options
    print('\nSelect the operation that you would like to perform:')
    print('1. View details of all parts')
    print('2. Add a new part')
    print('3. Change part quantity based on supplier')
    print('4. Change part quantity based on a warehouse\'s assembly section')
    print('5. Search')
    print('6. Inventory tracking')
    print('7. Help Page ')
    print('8. Exit')

    option = int (input('Enter selection: '))
    
    #determining which function to call
    if (option==1):
        viewPartDetails()
    elif (option==2):
        addPart()   
    elif (option==3):
        suppliersPartsTaken()
    elif (option == 4):
        assemblyPartsGiven()    
    elif (option==5):
        search()
    elif (option==6):
        tracking()         
    elif (option==7):
        helpPage()   
    elif (option == 8):
        print('Thank You, have a nice day')
    else:
        print('Invalid input')
        menu()


def allSections(lineOfPart):
    #section codes
    sectionList= ['BAS','CAS','IAS']
    #n is any 'number' for keeping count
    n=0
    for items in sectionList:
        if sectionList[n] in lineOfPart:
            if (n == 0):
                sec = "Body Assembly Section"
            elif (n == 1):
                sec = "Chassis Assembly Section"
            else:
                sec = "Interior Assembly Section"
    #printing section name
            print('Part of section: ',sec, end = "\t")
        n +=1


def viewPartDetails ():
    print ('\n')
    #viewing parts of warehouse1
    fileHandler = open('warehouse1.txt')
    warehouse1= fileHandler.readlines()
    #printing data for each part
    for line in warehouse1:
        line=line.strip()
        splitLine= line.split()
        partID = splitLine[0]
        print('Part ID: ', partID, end = "\t")
        units = splitLine [3]
        print('Quantity: ', units, end = "\t")
        #calling allSections function to print section of the part
        allSections(line)
        print('Part of warehouse:  Nissan Almera', end = "\n")
    fileHandler.close()
    print ('\n')


    #viewing parts of warehouse2
    fileHandler = open('warehouse2.txt')
    warehouse2= fileHandler.readlines()
    #printing data for each part
    for line in warehouse2:
        line=line.strip()
        splitLine= line.split()
        partID = splitLine[0]
        print('Part ID: ', partID, end = "\t")
        units = splitLine [3]
        print('Quantity: ', units, end = "\t")
        #calling allSections function to print section of the part
        allSections(line)
        print('Part of warehouse:  Nissan Murano', end = "\n")
    fileHandler.close()
    print ('\n')

    #viewing parts of warehouse3
    fileHandler = open('warehouse3.txt')
    warehouse3= fileHandler.readlines()
    #printing data for each part
    for line in warehouse3:
        line=line.strip()
        splitLine= line.split()
        partID = splitLine[0]
        print('Part ID: ', partID, end = "\t")
        units = splitLine [3]
        print('Quantity: ', units, end = "\t")
        #calling allSections function to print section of the part
        allSections(line)
        print('Part of warehouse:  Nissan X-Gear', end = "\n")
    fileHandler.close()
    print ('\n')  
    menu()


def addPart():
    #repeat based on number of parts that should be added
    newPartCount=int( input ('Enter the number of new parts you would like to add: '))
    for value in range(newPartCount):
        #create list for storing info about the new part
        info = ['1','1','1','1']
        # new part warehouse
        partWarehouse = str (input('Enter part warehouse number: '))
        if (partWarehouse == '1'):
            info[1]= 'WNAL'
        elif (partWarehouse == '2'):
            info[1]= 'WNMU'
        elif (partWarehouse == '3'):
            info[1]= 'WNXG'
        else:
            print ('wrong warehouse number; Enter part details again')
            newPartCount += 1
            break
        # new part assembly section
        partAssemblySection = str (input('Enter part assembly section number: '))
        if (partAssemblySection == '1'):
            info[2]= 'BAS'
        elif (partAssemblySection == '2'):
            info[2]= 'CAS'
        elif (partAssemblySection == '3'):
            info[2]= 'IAS'
        else:
            print ('wrong assembly section number; Enter part details again')
            newPartCount += 1
            break
        
        # new part quantity
        partQuantity = int (input('Enter part quantity: '))
        if (partQuantity > -1 ):
            info[3]= str(partQuantity)
        else:
            print ('invalid part quantity; Enter part details again')
            newPartCount += 1
            break
        
        # new part's ID     
        partID = str (input('Enter part ID (enter 1 to auto assign part ID): '))
        partID = partID.capitalize()
        # auto assinging part ID
        if (partID == '1'):
            autoPartID = ['P','a','b','c']
            autoPartID[1]= partWarehouse
            autoPartID[2]= partAssemblySection
            warehouseFile = str ('warehouse' + str (partWarehouse) + '.txt')
            fileHandler = open(warehouseFile,'r')
            sectionPartNumber= fileHandler.readlines()
            
            existingPartIDList = ['P', str( partWarehouse), str(partAssemblySection)]
            existingPartIDString = ''
            for elements in existingPartIDList:
                existingPartIDString += elements
               
            count = 0
            for lines in sectionPartNumber:
                if (existingPartIDString in lines):
                    count += 1
            autoPartID[3]= str(count + 1)
            
            autoPartIDString = ''
            for elements in autoPartID:
                autoPartIDString += elements
            
            fileHandler.close()
            info[0]= autoPartIDString 
            
        # manually assinging part ID        
        elif ((len (partID)  == 4)  and (partID[0] == 'P') and   ((partID[1] == '1') or (partID[1] == '2' ) or (partID[1] == '3' ))
              and  ((partID[2] == '1') or (partID[2] == '2' ) or (partID[2] == '3' ))  and (partID[3] != '0') ) :
            #divided in 2 lines due to its length being too long to display properly
            #no 0s possible in the part id
            warehouseFile = str ('warehouse' + str (partID[1]) + '.txt')
            fileHandler = open(warehouseFile,'r')
            warehousePartIDs= fileHandler.readlines()
            for line in warehousePartIDs:
                line=line.strip()
                splitLine= line.split()
                existingPartID = splitLine[0]
                if (partID == existingPartID ) :
                    print ('Part ID already exists (existing part details given below) ; Enter part details again')
                    print (line)
                    break
                    
            fileHandler.close()
            info[0]= partID   
            
        else:
            print ('invalid partID; Enter part details again')
            newPartCount += 1
            break

        #adding part info to file
        warehouseFile = str ('warehouse' + str (partWarehouse) + '.txt')
        fileHandler = open(warehouseFile,'a')
        fileHandler.write('\n')
        fileHandler.write(info[0])
        fileHandler.write('\t')
        fileHandler.write(info[1])
        fileHandler.write('\t')
        fileHandler.write(info[2])
        fileHandler.write('\t')
        fileHandler.write(info[3])
        fileHandler.close()

    menu()


def assemblyPartsGiven ():
    #changing part quantity based on assembly section
    # number of assembly sections that need their parts' quantites changed
    sectionAmount = int (input('Enter number of assembly sections to give parts to: '))
    for value in range (sectionAmount):
        #selecting warehouse of parts
        sectionWarehouse = str (input('Enter the assembly section\'s warehouse number: '))
        if (sectionWarehouse == '1'):
            warehouseNumber = 1
            warehouseName = 'Nissan Almera'
        elif (sectionWarehouse == '2'):
            warehouseNumber = 2
            warehouseName = 'Nissan Murano'
        elif (sectionWarehouse == '3'):
            warehouseNumber = 3
            warehouseName = 'Nissan X-Gear'
        else:
            print ('wrong warehouse number; Enter details again')
            break
        #selecting assembly section of parts
        assemblySection = str (input('Enter assembly section number: '))
        if (assemblySection == '1'):
            sectionName= 'BAS'
            sec = "Body Assembly Section"
        elif (assemblySection == '2'):
            sectionName= 'CAS'
            sec = "Chassis Assembly Section"
        elif (assemblySection == '3'):
            sectionName= 'IAS'
            sec = "Interior Assembly Section"
        else:
            print ('wrong assembly section number; Enter details again')
            break

        print('Warehouse chosen: ',warehouseName,'\t Section chosen: ',sec,'\n')

        warehouseFile = str ('warehouse' + str(warehouseNumber) + '.txt')
        fileHandler = open(warehouseFile,'r')
        warehouseLines= fileHandler.readlines()
        #displaying part IDs and quantities
        invalid = int (1)
        trackingLine = []
        newLine = []
        assemblyLines=[]
        for line in warehouseLines:
            line=line.strip()
            splitLine= line.split()
            if (sectionName in splitLine):
                partID = splitLine[0]
                partQuantity = splitLine[3]
                print ('part ID: ',partID,'\tcurrent quantity: ',partQuantity)
                newQuantity = int ( input ('enter new quantity of the part: ' ))
                if (newQuantity > -1 ):
                    splitLine[3] = str (newQuantity)
                    trackingLine.append(splitLine)
                else:
                    invalid = 2
                    break
            newLine.append(splitLine)
        #cancel writing if invalid input
        if (invalid == 1):
            fileHandler.close()
            fileHandler = open(warehouseFile,'w')
            for lines in newLine:
                for items in lines:
                    fileHandler.write(items)
                    fileHandler.write('\t')
                fileHandler.write('\n')
        else:
            print ('invalid part quantity')
            invalid = 1

        fileHandler.close()
        fileHandler = open('sectionTracking.txt','a')
        for lines in trackingLine:
            for items in lines:
                fileHandler.write(items)
                fileHandler.write('\t')
            fileHandler.write('\n')
        fileHandler.close()
    menu()


def suppliersPartsTaken ():
    #changing part quantity based on supplier
    fileHandler = open('suppliers.txt')
    supplierInfo= fileHandler.readlines()
    #supplier identification
    supplierToFind = str( input ('Enter Supplier name or ID: '))
    supplierToFind = supplierToFind.capitalize()
    #finding the supplier
    supplierLine=[]
    for line in supplierInfo:
        line=line.strip()
        splitLine= line.split()
        supplierID = splitLine[0]
        supplierName = splitLine[-1]
        if (supplierToFind == supplierID) or (supplierToFind == supplierName):
            supplierLine = splitLine          
    if (supplierLine == []):
        print ('supplier not found')
    else:
    #updating quantities of parts supplied by the supplier
        supplierParts = supplierLine [1:-1]
        print ('supplied parts: ', supplierParts)
        supplierWarehouse = (supplierLine[0][1])
        warehouseFile = str ('warehouse' + str(supplierWarehouse) + '.txt')
        invalid = int (1)
        for parts in supplierLine:
            newLine = []
            fileHandler = open(warehouseFile,'r')
            partsOfSupplier= fileHandler.readlines()
            for line in partsOfSupplier:
                line=line.strip()
                splitLine= line.split()
                partID = splitLine[0]
                partQuantity = splitLine[3]
                if (partID in parts):
                    print ('part ID: ',partID,'; current quantity: ',partQuantity)
                    newQuantity = int ( input ('enter new quantity of the part: ' ))
                    if (newQuantity > -1 ):
                        splitLine[3] = str (newQuantity)
                    else:
                        invalid = 2
                        break
                newLine.append(splitLine)
            # checking valididity
            if (invalid == 1):
                fileHandler.close()
                fileHandler = open(warehouseFile,'w')
                for lines in newLine:
                    for items in lines:
                        fileHandler.write(items)
                        fileHandler.write('\t')
                    fileHandler.write('\n')
            else:
                print ('invalid part quantity')
                invalid = 1
            fileHandler.close()
    menu()


def search ():
    #search options
    print ('enter 1 to search a part’s record')
    print ('enter 2 to search supplier details for a part')
    print ('enter 3 to search the parts supplied by a supplier')
    
    choice = int(input('Enter selection: '))
    
    if (choice==1):
    #specific part's details
        searchAttempts= int (input ('Enter number of parts to search: '))
        for value in range(searchAttempts):
            partSearchID=str ( input ('Enter part ID to search: '))
            partSearchID = partSearchID.capitalize()
            error = 1
            if ((len (partSearchID)  == 4)  and (partSearchID[0] == 'P') and  ((partSearchID[1] == '1') or (partSearchID[1] == '2' ) or (partSearchID[1] == '3' )) and  ((partSearchID[2] == '1') or (partSearchID[2] == '2' ) or (partSearchID[2] == '3' ))   and ('0' not in partSearchID) ) : #no 0s possible in the part id
                warehouseFile = str ('warehouse' + str (partSearchID[1]) + '.txt')
                fileHandler = open(warehouseFile,'r')
                warehousePartIDs= fileHandler.readlines()
                for line in warehousePartIDs:
                    line=line.strip()
                    splitLine= line.split()
                    existingPartID = splitLine[0]
                    if (partSearchID == existingPartID ) :
                        print('Part ID: ', partSearchID, end = "\t")
                        units = splitLine [3]
                        print('Quantity: ', units, end = "\t")
                        allSections(line)
                        if (partSearchID[1] == '1'):
                            warehouseName = 'Nissan Almera'
                        elif (partSearchID[1] == '2'):
                            warehouseName = 'Nissan Murano'
                        elif (partSearchID[1] == '3'):
                            warehouseName = 'Nissan X-Gear'
                        print('Part of warehouse:', warehouseName, end = "\n")
                        error = 0
                        break
                fileHandler.close()
                if (error != 0):
                    print ('partID not found')
                    fileHandler.close()
            else:
                print ('invalid partID')
       
    elif (choice==2):
    #supplier details of a part
        searchAttempts= int (input ('Enter number of parts\' suppliers to search: '))
        for value in range(searchAttempts):
            partSearchID=str ( input ('Enter part ID to search its supplier: '))
            partSearchID = partSearchID.capitalize()
            error = 1
            if ((len (partSearchID)  == 4)  and (partSearchID[0] == 'P') and  ((partSearchID[1] == '1') or (partSearchID[1] == '2' ) or (partSearchID[1] == '3' )) and  ((partSearchID[2] == '1') or (partSearchID[2] == '2' ) or (partSearchID[2] == '3' ))   and ('0' not in partSearchID) ) : #no 0s possible in the part id
                fileHandler = open('suppliers.txt','r')
                suppliersAll= fileHandler.readlines()
                for line in suppliersAll:
                    line=line.strip()
                    splitLine= line.split()
                    supplierParts = splitLine [1:-1]
                    if (partSearchID in supplierParts ) :
                        supplierID = splitLine[0]
                        print ('Supplier ID: ',supplierID)
                        supplierName = splitLine[-1]
                        print ('Supplier name: ',supplierName)
                        print ('Parts supplied by supplier: ',supplierParts)
                        error = 0
                fileHandler.close() 
                if (error != 0):
                    print ('partID not found')
                    fileHandler.close()
            else:
                print ('invalid partID')   
    elif (choice==3):
    #supplier's details
        searchAttempts= int (input ('Enter number of suppliers to search: '))
        for value in range(searchAttempts):
            invalid = int(1)
            supplierSearchID=str ( input ('Enter Supplier name or ID to search: '))
            supplierSearchID = supplierSearchID.capitalize()
            fileHandler = open('suppliers.txt','r')
            suppliersAll= fileHandler.readlines()
            for line in suppliersAll:
                line=line.strip()
                splitLine= line.split()
                supplierID= splitLine[0]
                supplierName = splitLine[-1]
                if (supplierSearchID == supplierID ) or (supplierSearchID == supplierName) :
                    print ('Supplier ID: ',supplierID)
                    print ('Supplier name: ',supplierName)
                    supplierParts = splitLine [1:-1]
                    print ('Parts supplied by supplier: ',supplierParts)
                    invalid = 0
            if (invalid == 1):
                print ('did not find any supplier with the given name or ID') 
    else:
        print('Invalid input')
    fileHandler.close()         
    menu()


def tracking():
    #inventory tracking options
    print ('enter 1 to view all parts and their quantity')
    print ('enter 2 to view all parts with low quantities')
    print ('enter 3 to view the parts and quantity provided to each assembly section by warehouse')
    choice = int(input('Enter selection: '))
    if (choice==1):
    #displaying all parts and quantities 
        #viewing parts of warehouse1
        print ('')
        fileHandler = open('warehouse1.txt')
        warehouse= fileHandler.readlines()
        warehouse.sort()
        for line in warehouse:
            line=line.strip()
            splitLine= line.split()
            partID = splitLine[0]
            print('Part ID: ', partID, end = "\t")
            units = splitLine [3]
            print('Quantity: ', units, end = "\n")
        fileHandler.close()

        #viewing parts of warehouse2
        print ('')
        fileHandler = open('warehouse2.txt')
        warehouse= fileHandler.readlines()
        warehouse.sort()
        for line in warehouse:
            line=line.strip()
            splitLine= line.split()
            partID = splitLine[0]
            print('Part ID: ', partID, end = "\t")
            units = splitLine [3]
            print('Quantity: ', units, end = "\n")
        fileHandler.close()

        #viewing parts of warehouse3
        print ('')
        fileHandler = open('warehouse3.txt')
        warehouse= fileHandler.readlines()
        warehouse.sort()
        for line in warehouse:
            line=line.strip()
            splitLine= line.split()
            partID = splitLine[0]
            print('Part ID: ', partID, end = "\t")
            units = splitLine [3]
            print('Quantity: ', units, end = "\n")
        fileHandler.close()
        menu()

    elif (choice==2):
    #showing parts with low quantity
        print ('Parts with quantity less than 10: ')
        #viewing parts of warehouse1
        fileHandler = open('warehouse1.txt')
        warehouse= fileHandler.readlines()
        warehouse.sort()
        for line in warehouse:
            line=line.strip()
            splitLine= line.split()
            partID = splitLine[0]
            units = int (splitLine [3])
            if (units < 10):
                print('Part ID: ', partID, end = "\t")
                print('Quantity: ', units, end = "\n")
        fileHandler.close()
        
        #viewing parts of warehouse2
        fileHandler = open('warehouse2.txt')
        warehouse= fileHandler.readlines()
        warehouse.sort()
        for line in warehouse:
            line=line.strip()
            splitLine= line.split()
            partID = splitLine[0]
            units = int (splitLine [3])
            if (units < 10):
                print('Part ID: ', partID, end = "\t")
                print('Quantity: ', units, end = "\n")
        fileHandler.close()
        
        #viewing parts of warehouse3
        fileHandler = open('warehouse3.txt')
        warehouse= fileHandler.readlines()
        warehouse.sort()
        for line in warehouse:
            line=line.strip()
            splitLine= line.split()
            partID = splitLine[0]
            units = int (splitLine [3])
            if (units < 10):
                print('Part ID: ', partID, end = "\t")
                print('Quantity: ', units, end = "\n")
        fileHandler.close()
        menu()

    elif (choice==3):
    #track of all part quantities updated based on assembly section
        print ('\nList of parts with quantity sent to assembly sections: \n')
        fileHandler = open('sectionTracking.txt')
        track= fileHandler.readlines()
        track.sort()
        for line in track:
            line=line.strip()
            splitLine= line.split()
            partID = splitLine[0]
            print('Part ID: ', partID, end = "\t")
            units = splitLine[3]
            print('Quantity: ', units, end = "\t")
            partWarehouse = splitLine[1]
            if (partWarehouse == 'WNAL'):
                warehouseName = 'Nissan Almera'
            elif (partWarehouse == 'WNMU'):
                warehouseName = 'Nissan Murano'
            else:
                warehouseName = 'Nissan X-Gear'
            print('Part of warehouse:',warehouseName, end = "\t")
            allSections(line)
            print('')
        fileHandler.close()
        menu()
    else:
        print('Invalid input')

  
def helpPage(): 
    #info about how to use the program
    print('\nHelp Page')
    print('Parts: ')
    print('\t Part ID structure: ')
    print('\t first character = \'P\' ; stands for Part ')
    print('\t second character = 1 or 2 or 3 ; stands for the corresponding warehouse number ')
    print('\t third character = 1 or 2 or 3 ; stands for the corresponding assembly section number ')
    print('\t fourth character = 1 to 9 ; stands for Part number ')
    print('\t Part Quantity can only be at or above 0')
    print('\t no more than 9 parts in each assembly section')


    print('Warehouses: ')
    print('\t warehouse numbers: ')
    print('\t Nissan Almera warehouse = 1')
    print('\t Nissan Murano warehouse = 2')
    print('\t Nissan X-Gear warehouse = 3')

    print('Assembly Sections: ')
    print('\t Section numbers: ')
    print('\t Body Assembly Section = 1')
    print('\t Chassis Assembly Section = 2')
    print('\t Interior Assembly Section = 3')
    menu()


#running code
print('for first time users, kindly visit the help page by entering 7 as it has the details about the parts, warehouses, etc.')
menu()
