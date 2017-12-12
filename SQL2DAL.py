# -*- coding: utf-8 -*-
# vi:ts=4:et

SQL='''SELECT "Секретарь", "номер группы", "Нет оценки рецензента", "Нет рецензента", 
       "Оценка без рецензента", "Без дня защиты"
  FROM "Диплом"."Статистика для секретаря";'''
import parse
filtred_SQL=SQL.replace("\n","") # удалить символы новой строки
поля,таблица=parse.parse("SELECT {} FROM {};",filtred_SQL) # выделить список полей и имя таблицы
fields=поля.split(",")
# объявление таблицы для DAL
declare4DAL='''db.define_table('',
%s
                rname='%s',
                primarykey=[''],
                migrate=False
               )'''%("\n".join(['''Field('',rname='%s',type='string',label=%s),'''%(field.strip(),field.strip(),) for field in поля.split(",")]),таблица.strip(),)

print(declare4DAL)