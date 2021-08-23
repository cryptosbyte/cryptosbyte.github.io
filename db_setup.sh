echo ">>>>>> Initialising SQL Alchemy Database <<<<<<"
python3 -c "from app import db; db.create_all()"
# -c option allows Python3 to run, well Python3 code, in the CLI
echo ">>>>>> SQL Database has been initialised <<<<<<"