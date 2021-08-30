import pymysql 

class MySQLData() : 

    def __init__( self ) : 
        
        #建立MySQL 資料庫#######################################
        self.myclient = pymysql.connect( host     = "127.0.0.1",
                                         user     = "root",
                                         password = "john",
                                         database = "sites",
                                         charset  = "utf8" )
        #######################################################

    def __str__( self ) : 

        with self.myclient.cursor() as cursor :

            command = "SELECT * FROM charts"
            cursor.execute(command)
        
            result = cursor.fetchall()
    
            return "\n".join( map( str , result ) )

    def show_data( self ) :

        with self.myclient.cursor() as cursor :

            command = "SELECT * FROM charts"
            cursor.execute(command)
        
            result = cursor.fetchall()
    
            return result
 

    def insert_data( self , data ) :

        key   = str( list( data.keys() ) ).replace( '\'' , "" )[1:-1]  
        value = str( [ str(x) for x in data.values() ] )[1:-1]
        
        with self.myclient.cursor() as cursor :
            
            cursor.execute( f"INSERT INTO charts( {key} )VALUES( {value} )")
            self.myclient.commit()
        
        print( "資料新增成功" )

    def get_data( self , data ) : 

        key   = list(data.keys())[0]
        value = list(data.values())[0]
       
        with self.myclient.cursor() as cursor :

            cursor.execute( f"SELECT * FROM charts WHERE {key} = '{value}' " )
            result = cursor.fetchall()
            self.myclient.commit()

        return result

    def delete_data( self , data ) :

        key   = list(data.keys())[0]
        value = list(data.values())[0]
       
        with self.myclient.cursor() as cursor :

            cursor.execute( f"DELETE FROM charts WHERE {key} = '{value}' " )
            self.myclient.commit()
        
        print( "刪除成功" )


if __name__ == "__main__" :

    client = MySQLData()
    
    print( client )
    print( "-"*50)

    print( client.get_data( { "Title" : "NewsB" } ) )
    print( "-"*50)

    for i in range(10) : 
        client.insert_data( {"Author": "test", "Title": "test", "Tags":"test", "Detail": "test" , 'Date':'2021/9/9' } ) 
    print( client )
    print( "-"*50)
    
    client.delete_data( { "Title" : "test" } )
    print( client )