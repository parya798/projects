from flask import jsonify 
from memory.db_handler import Database 
from memory.services import RamStatsService 
from memory.api import app 

if __name__ == "__main__": 
    db = Database("memory/ram_stats.db") 
    db.initialize_db() 
    
    RamStatsService.record_ram_stats("memory/ram_stats.db") 
    
    app.run("0.0.0.0", 3000)