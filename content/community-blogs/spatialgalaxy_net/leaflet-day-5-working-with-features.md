---
source: "blog"
title: "Leaflet Day 5 - Working with Features"
image: "leaflet-day-5-working-with-features"
date: "2019-01-27T05:19:21-0900"
link: "http://spatialgalaxy.net/2019/01/27/leaflet-day-5-working-with-features/"
draft: "true"
showcase: "planet"
folder: "spatialgalaxy_net"
author: "Spatial Galaxy"
---

Today we&rsquo;ll add towns along the trail route that are mentioned in the novels. I hesitate to call them towns, because in 1902, many of them consisted of a view indigenous people and sometimes a roadhouse.
The method to add these locations will be to add a GeoJSON layer and loop through each town, adding a marker and popup with some info.
The Data The data for the locations is from the GNIS database for Alaska, containing over 35,000 locations.
