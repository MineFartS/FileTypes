from philh_myftp_biz.file import JSON, temp
from philh_myftp_biz.array import List
from philh_myftp_biz.json import Dict
from philh_myftp_biz.pc import Path

#
tempfile = temp('mimetypes', 'json')

# Init raw db
raw: List[dict] = List(JSON(Path("mimetype-io/src/mimeData.json")))

# Init override db
override: Dict[str] = Dict(JSON(Path('override.json')))

# Init compiled db
compiled: Dict[str] = Dict(JSON(Path('compiled.json')))

# Reset compiled db
compiled.save({})

#
for data in raw:

    if ('name' in data) and ('/' in data['name']):

        #
        type = data['name'].split('/')[0]

        #
        for ext in data['fileTypes']:

            #
            compiled[ext[1:]] = type

#
for ext, type in override.items():
    
    #
    compiled[ext] = type