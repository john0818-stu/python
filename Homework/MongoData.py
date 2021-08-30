import pymongo 

class MongoData() : 

    def __init__( self , mydbname , colname ) : 
        
        self.myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        self.mydb     = self.myclient[ mydbname ]       # 資料庫名稱
        self.mycol    = self.mydb[ colname ]            # 資料夾名稱

    def __str__( self ) : 

        print("目前存在的DB有 : "     , self.myclient.list_database_names() )
        return f"目前存在的資料庫有 : {self.mydb.list_collection_names()}"

    def insert_data( self , data ) : 

        try : 
            self.mycol.insert_one( data ) 
            print("資料新增成功")

        except pymongo.errors.DuplicateKeyError : 
            return "資料增加失敗 有重複資料"

    def updata_data( self , old_data , new_data ) :

        try :     
            self.mycol.update_one( old_data , new_data ) 
            print( "更新成功" )
        except pymongo.errors.DuplicateKeyError :  
            return "資料更新失敗 有重複資料"

    def get_data( self, data = {} ) : #空白全部搜尋

        return self.mycol.find( data )

    def delete_data( self , data ) : 

        self.mycol.delete_one( data ) 
        print( "刪除成功" )

    def set_index( self , name ) : 
        
        self.mycol.create_index( name , unique = True  )

    def data2json( self , name ) : 

        for dic in self.mycol.find( name ) : 
            data = dic  
    
        import json
        with open( f"{ list(name.values())[0] }.json" , "w" ) as outfile : 

            data.pop( "_id" )

            json.dump( data , outfile ) 

        print( "已轉成Json檔" )
        

if __name__ == "__main__" : 

    client = MongoData( "runoobdb" , "sites" )

    '''
    client.set_index( "Author" ) 
    client.set_index( "Title" ) 
   
    print( client )
    client.insert_data( { "Author" : "Andy" , "Title": "NewsA", "Tags": ["Gossiping"] ,       "Detail": {  "Content": "Taiwan NO.1" } } )
    client.insert_data( { "Author" : "Andy" , "Title": "NewsC", "Tags": ["Gossiping"] ,       "Detail": {  "Content": "Taiwan NO.1" } } )
    client.insert_data( { "Author" : "hhh"  , "Title": "NewsB", "Tags": ["Social", "Wally"] , "Detail": {  "Content": "NO.1" } } )
    client.insert_data( { "Author" : "test" , "Title": "NewsB", "Tags": ["Gossiping"] ,       "Detail": {  "Content": "Taiwan NO.1" } } )
    '''

    for lis in client.get_data( {"Title": "NewsH" }) : 
        print( lis )    

    '''
    old_data = { "Title": "NewsA" }
    new_data = { "$set" : {"Title": "NewsZ" } }

    client.updata_data( old_data , new_data ) 
    
    client.delete_data(  { "Tags": ["Gossiping"] } )
    print( client.get_data() )
    '''

    client.data2json( {"Title" : "NewsB"} )