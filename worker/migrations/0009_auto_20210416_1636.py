# Generated by Django 3.1.7 on 2021-04-16 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0008_auto_20210416_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='experience',
            field=models.CharField(choices=[(0, 1940), (1, 1941), (2, 1942), (3, 1943), (4, 1944), (5, 1945), (6, 1946), (7, 1947), (8, 1948), (9, 1949), (10, 1950), (11, 1951), (12, 1952), (13, 1953), (14, 1954), (15, 1955), (16, 1956), (17, 1957), (18, 1958), (19, 1959), (20, 1960), (21, 1961), (22, 1962), (23, 1963), (24, 1964), (25, 1965), (26, 1966), (27, 1967), (28, 1968), (29, 1969), (30, 1970), (31, 1971), (32, 1972), (33, 1973), (34, 1974), (35, 1975), (36, 1976), (37, 1977), (38, 1978), (39, 1979), (40, 1980), (41, 1981), (42, 1982), (43, 1983), (44, 1984), (45, 1985), (46, 1986), (47, 1987), (48, 1988), (49, 1989), (50, 1990), (51, 1991), (52, 1992), (53, 1993), (54, 1994), (55, 1995), (56, 1996), (57, 1997), (58, 1998), (59, 1999), (60, 2000), (61, 2001), (62, 2002), (63, 2003), (64, 2004), (65, 2005), (66, 2006), (67, 2007), (68, 2008), (69, 2009), (70, 2010), (71, 2011), (72, 2012), (73, 2013), (74, 2014), (75, 2015), (76, 2016), (77, 2017), (78, 2018), (79, 2019), (80, 2020)], max_length=50, null=True, verbose_name='Стаж'),
        ),
    ]