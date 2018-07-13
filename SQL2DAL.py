# -*- coding: utf-8 -*-
# vi:ts=4:et

SQL='''
'''
import parse
filtred_SQL=SQL.replace("\t"," ").replace("\n","") # удалить символы новой строки
поля,таблица=parse.parse("SELECT {} FROM {};",filtred_SQL) # выделить список полей и имя таблицы
fields=поля.split(",")
# объявление таблицы для DAL
declare4DAL='''db.define_table('',
%s
                rname='%s',
                primarykey=[''],
                migrate=False
               )'''%("\n".join(['''Field('', rname='%s', type='string', label=%s),'''%(field.strip(),field.strip(),) for field in поля.split(",")]),таблица.strip(),)

print(declare4DAL)
