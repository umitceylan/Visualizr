# -*- coding: utf-8 -*-

import os

"""def retrieve_file(filename, path=None):
    path = "applications/Visualizr/static"
    return (filename, open(os.path.join(path, filename), 'rb'))"""

db.define_table('master_table',
             Field('person'),
             Field('upload_data', 'upload', uploadfolder=os.path.join(request.folder, 'static')),
             Field('table_id'))
