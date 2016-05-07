# -*- coding: utf-8 -*-

import os

db.define_table('master_table',
             Field('person'),
             Field('upload_data', 'upload', uploadfolder=os.path.join(request.folder, 'static')),
             Field('tablename'))
