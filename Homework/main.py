from flask import Flask , render_template , request
import json

import module , MongoData , MySQLData

app = Flask( __name__ )

@app.route('/')
def home() : 
    return render_template( "home.html" )

@app.route( "/findWally" )
def findWally() : 
    
    data = module.get_json( "client1" )
    return "<br>".join( [ str(dic) for dic in data ] )

@app.route( "/createNews" ) 
def createNews() : 

    client = MongoData.MongoData( "runoobdb" , "sites" )
    client.set_index( "Title" )
    client.set_index( "Author" )

    data = module.get_json( "client1" )
        
    for dic in data : 
                    
        if str( client.insert_data( dic ) ) == "資料增加失敗 有重複資料" : 
            
            return client.insert_data( dic )

    return "資料增加，存入成功"


@app.route( "/findNews" , methods = [ "POST" , "GET" ] )
def findNews() : 

    if request.method == "POST" : 

        client = MongoData.MongoData( "runoobdb" , "sites" )
        name = request.values.get( "content" )

        for dic in client.get_data( { "Author" : name } ) :
            return dic["Title"]  

    return render_template( "findNews.html" )

@app.route( "/Mongo2MySQL" , methods = [ "POST" , "GET" ] )
def Mongo2MySQL() : 
    
    if request.method == "POST" :   
        
        client = MongoData.MongoData( "runoobdb" , "sites" )
        contkey = request.values.get( "contentkey" )
        contvalue = request.values.get( "contentvalue" )

        client.data2json( { contkey : contvalue } ) 
    
        json_infile = open( contvalue + ".json" , "r" )
        data = json.loads( json_infile.read() ) 

        SQLclient = MySQLData.MySQLData()
        SQLclient.insert_data( data )

        return "儲存成功"
    
    return render_template( "Mongo2MySQL.html" )

@app.route( "/save_mongo" , methods = [ "POST" , "GET" ])
def save_mongo() : 

    if request.method == "POST" :   

        dic = { x : request.values.get(x) for x in request.values }

        client = MongoData.MongoData( "runoobdb" , "sites" )

        if str( client.insert_data( dic ) ) == "資料增加失敗 有重複資料" : 
            
            return client.insert_data( dic )

        return "資料增加，存入成功"

    return render_template( "save_mongo.html" )

@app.route( "/ALL_Mongo" )
def all_Mongo() : 

    client = MongoData.MongoData( "runoobdb" , "sites" )
    return "<br>".join( [ str(dic) for dic in client.get_data() ] )

@app.route( "/ALL_MySQL" )
def ALL_MySQL() : 

    SQLclient = MySQLData.MySQLData()
    return "<br>".join( [ str(dic) for dic in SQLclient.show_data() ] )



if __name__ == "__main__" : 
    
    app.run( debug = True ) 