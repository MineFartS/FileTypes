from philh_myftp_biz.file import JSON, temp
from philh_myftp_biz.web import download
from philh_myftp_biz.array import List
from philh_myftp_biz.json import Dict
from philh_myftp_biz.pc import Path

#
tempfile = temp('mimetypes', 'json')

#
download(
    url = 'https://raw.githubusercontent.com/patrickmccallum/mimetype-io/refs/heads/master/src/mimeData.json',
    path = tempfile
)

#
raw: List[dict] = List(JSON(tempfile))

#
override: Dict[str] = Dict(JSON(Path('override.json')))

#
compiled: Dict[str] = Dict(JSON(Path('compiled.json')))
#
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