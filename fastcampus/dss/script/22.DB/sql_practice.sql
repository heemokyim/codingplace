select city.name, country.code, country.name, city.population, country.population,
round(city.population / country.population * 100) as percentage
from (select * from city where population > 5000000) as city
join country
on city.countrycode = country.code
having percentage > 10 
order by percentage desc

select code, name, surfacearea, population, round(population/surfacearea) as density, count(language) as lang
from country
join countrylanguage
on country.code = countrylanguage.CountryCode
where surfacearea >= 10000
group by name
having density >= 200
order by lang desc


select city.countrycode, city.name, city.population, country.name, city.language_count, city.languages
from 
(select city.countrycode, city.name, city.population,cl.language_count, languages
from
(select countrycode, group_concat(language) as languages, count(language) as language_count
from countrylanguage
group by countrycode
having language_count<=3
) as cl
join (select * from city where population > 3000000) as city
on city.countrycode = cl.countrycode
) as city
join country
on city.countrycode = country.code
