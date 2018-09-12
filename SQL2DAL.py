# -*- coding: utf-8 -*-
# vi:ts=4:et

SQL='''
        SELECT "код", "Кафедра"
	FROM "Диплом"."Список направлений";
'''
замена={ # подстановка имен полей
"Кафедра":'kaf',
"Семестр":'semestr',
"Форма":'form',
"номер группы":'group',
"группа":'group',
"Направление":'napravl',
"Профиль":'profile',
"направление":'napravl',
"профиль":'profile',
"№ приказа":'N_prikaza',
"Дата приказа":'date',
"Секретарь":'secretary',
"председатель":'predsed',
"вид":'vid',
"вид приказа":'vid_prikaza',
"Вид приказа":'vid_prikaza',
"id":'id',
"дата":'date',
}
import parse
filtred_SQL=SQL.replace("\t"," ").replace("\n","").strip() # удалить символы новой строки
поля,таблица=parse.parse("SELECT {} FROM {};",filtred_SQL) # выделить список полей и имя таблицы
fields=поля.split(",")
# объявление таблицы для DAL
declare4DAL='''db.define_table('',
%s
                rname='%s',
                primarykey=[''],
                migrate=False
               )'''%("\n".join(['''Field('%s', rname='%s', type='string', label=%s),'''%(замена.get(field.strip().replace('"', ''), ''), field.strip(), field.strip()) for field in поля.split(",")]),таблица.strip(),)

print(declare4DAL)
# Сетка для контроллера
grid='''def ():
'''+"   '''  '''"+'''
   grid=SQLFORM.grid(db.$$, # источник данных
                    details=False,csv=False, # нужна только сетка
                    searchable=False,
                    fields=(%s), #
                    paginate=0, # без разбивки на страницы
                    #maxtextlengths={"napravl":10},
                    #orderby= # поля, которые выводятся
                   )
   return dict(grid=grid)
'''%(", ".join(['''db.$$.%s'''%(замена.get(field.strip().replace('"', ''), field.strip()),) for field in поля.split(",")]),)
print(grid)
