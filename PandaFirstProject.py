import pandas as pas
import logging as lgg


def CopyDataToNewFile():
    try:
        lgg.basicConfig(format='\nLog created: %(asctime)s\n%(message)s',
                        filename='C:/Users/Name/Downloads/logfile.log',
                        level=lgg.DEBUG, datefmt='%m-%d-%Y %I:%M:%S %p', encoding='utf-8')
    #Read Original and New files
        FileToUpdate = pas.read_excel("C:/Users/Name/Downloads/Book Inventory.xlsx")
        FileWithNewData = pas.read_excel("C:/Users/Name/Downloads/Book Inventory 2.xlsx")
    #Map the files to a DataFrame
        UpdateFileDataFrame = pas.DataFrame(FileToUpdate)
        NewFileDataFrame = pas.DataFrame(FileWithNewData)
    #Merge the two DataFrames in a list, so pandas can use concat then remove duplicate values
        ffaa = [UpdateFileDataFrame, NewFileDataFrame]
        ffaaout = pas.DataFrame.drop_duplicates(pas.concat(ffaa))
    #Set the index to the first column, this one is named "Title"
        ffaaout.set_index("Title",inplace=True)
    #Write the concatenated list to the Original file
        ffaaout.to_excel("C:/Users/Chris/Downloads/Book Inventory.xlsx")
    #Log the updates
        lgg.info(f'OriginalDataLength: {len(FileToUpdate)}'
                 f'\nNewDataLength: {len(FileWithNewData)}'
                 f'\nConcatDataLength: {len(ffaaout)}'
                 f'\nNewRowCount: {len(ffaaout)-len(FileToUpdate)}')
        print('No Errors')
    #Log errors if they occur
    except FileNotFoundError as fnferr:
        lgg.error(f'ErrorThrown: FileNotFoundError'
                  f'\nLocation: {fnferr.filename}')
CopyDataToNewFile()