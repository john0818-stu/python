import json

def get_json( file_name ) : 
    
    json_infile = open( file_name + ".json" , "r" )
    data = json.loads( json_infile.read() ) 
    
    ans_lis = [] 
    for dic in data["News"] : 
        
        author = dic["Detail"]["Author"]
        
        del dic["Detail"]["Author"]
        dic["Author"] = author

        ans_lis += [ dic ]

    json_infile.close() 
    
    return ans_lis 



if __name__ == "__main__" : 
    
    lis = get_json( "client1" )
    print( lis )