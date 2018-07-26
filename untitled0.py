# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 20:58:23 2018

@author: yanghe
"""

import os
cmd1 = 'java -Xmx1024m -Dfile.encoding=UTF-8 -classpath ".;fnlp-core/target/fnlp-core-2.1-SNAPSHOT.jar;libs/trove4j-3.0.3.jar;libs/commons-cli-1.2.jar" org.fnlp.nlp.cn.tag.CWSTagger -s models/seg.m "%s"'%str('胜多负少')
cmd = 'dir'
d = os.popen(cmd1)
print(d.read())