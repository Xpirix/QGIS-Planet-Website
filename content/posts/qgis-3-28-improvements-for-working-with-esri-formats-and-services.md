---
source: "blog"
title: "QGIS 3.28 improvements for working with ESRI formats and services"
date: "2022-11-24T04:33:47+0000"
link: "https://north-road.com/2022/11/24/qgis-3-28-improvements-for-working-with-esri-formats-and-services/"
draft: "false"
showcase: "planet"
subscribers: ["north_road"]
author: "North Road"
tags: ["qgis", "esri", "geospatial", "osgeo", "qgis"]
languages: ["en_gb"]
available_languages: ["en_gb"]
---

<p>The QGIS 3.28 release is an extremely exciting release for all users who work in mixed software workplaces, or who need to work alongside users of ESRI software. In this post we’ll be giving an overview of all the new tools and features introduced in 3.28 which together result in a dramatic improvement in the workflows and capabilities in working with ESRI based formats and services. Read on for the full details…!</p>
<p>Before we begin, we’d like to credit the following organisations for helping fund these developments in QGIS 3.28:</p>
<ul>
<li>Naturstyrelsen, Denmark</li>
<li>Provincie Gelderland, Netherlands</li>
<li>Uppsala Universitet, Department of Archaeology and Ancient History</li>
<li>Gemeente Amsterdam</li>
<li>Provincie Zuid-Holland, Netherlands</li>
</ul>
<h2>FileGeodatabase (GDB) related improvements</h2>
<p>The headline item here is that QGIS 3.28 introduces support for editing, managing and creating ESRI FileGeodatabases out of the box! While older QGIS releases offered some limited support for editing FileGeodatabase layers, this required the manual installation of a closed source ESRI SDK driver… which unfortunately resulted in other regressions in working with FileGeodatabases (such as poor layer loading speed and random crashes). Now, thanks to an incredible reverse engineering effort by the <a href="https://gdal.org/">GDAL</a> team, the <a href="https://gdal.org/drivers/vector/openfilegdb.html">open-source driver for FileGeodatabases</a> offers <strong>full</strong> support for editing these datasets! This means all QGIS users have out-of-the-box access to a fully functional, high-performance read AND write GDB driver, no further action or trade-offs required.</p>
<p>Operations supported by the GDAL open source driver include:</p>
<ul>
<li>Editing existing features, with full support for editing attributes and curved, 3D and measure-value geometries</li>
<li>Creating new features</li>
<li>Deleting features</li>
<li>Creating, adding and modifying attributes in an existing layer</li>
<li>Full support for reading and updating spatial indexes</li>
<li>Creating new indexes on attributes</li>
<li>“Repacking” layers, to reduce their size and improve performance</li>
<li>Creating new layers in an existing FileGeodatabase</li>
<li>Removing layers from FileGeodatabases</li>
<li>Creating completely new, empty FileGeodatabases</li>
<li>Creating and managing field domains</li>
</ul>
<p>On the QGIS side, the improvements to the GDAL driver meant that we could easily expose feature editing support for FileGeodatabase layers for all QGIS users. While this is a huge step forward, especially for users in mixed software workplaces, we weren’t happy to rest there when we  had the opportunity to further improve GDB support within QGIS!</p>
<p>So in QGIS 3.28 we also introduced the following new functionality when working with FileGeodatabases:</p>
<h3>FileGeodatabase management tools</h3>
<p>QGIS 3.28 introduces a whole range of GUI based tools for managing FileGeodatabases. To create a brand new FileGeodatabase, you can now right click on a directory from the QGIS Browser panel and select New – ESRI FileGeodatabase:</p>
<p><img alt="" class="alignnone size-full wp-image-212448" height="405" src="/img/subscribers/north_road/qgis-3-28-improvements-for-working-with-esri-formats-and-services/create_geodatabase.webp" width="615"/></p>
<p>After creating your new database, a right click on its entry will show a bunch of available options for managing the database. These include options for creating new tables, running arbitrary SQL commands, and database-level operations such as compacting the database:</p>
<p><img alt="" class="alignnone size-full wp-image-212449" height="349" src="/img/subscribers/north_road/qgis-3-28-improvements-for-working-with-esri-formats-and-services/new_table.webp" width="528"/></p>
<p>You’re also able to directly import existing data into a FileGeodatabase by simply dragging and dropping layers onto the database!</p>
<p>Expanding out the GDB item will show a list of layers present in the database, and present options for managing the fields in those layers. Alongside field creation, you can also remove and rename existing fields.</p>
<p><img alt="" class="alignnone size-full wp-image-212450" height="218" src="/img/subscribers/north_road/qgis-3-28-improvements-for-working-with-esri-formats-and-services/create_field.webp" width="589"/></p>
<h3>Field domain handling</h3>
<p>QGIS 3.28 also introduces a range of GUI tools for working with field domains inside FileGeodatabases. (GeoPackage users also share in the love here — these same tools are all available for working with field domains inside this standard format too!) Just right click on an existing FileGeodatabase (or GeoPackage) and select the “New Field Domain” option. Depending on the database format, you’ll be presented with a list of matching field domain types:</p>
<p><img alt="" class="alignnone size-full wp-image-212451" height="289" src="/img/subscribers/north_road/qgis-3-28-improvements-for-working-with-esri-formats-and-services/new_field_domain.webp" width="777"/></p>
<p>Once again, you’ll be guided through a user-friendly dialog allowing you to create your desired field domain!</p>
<p><img alt="" class="alignnone size-full wp-image-212452" height="568" src="/img/subscribers/north_road/qgis-3-28-improvements-for-working-with-esri-formats-and-services/Screenshot-from-2022-11-24-12-46-17.webp" width="401"/></p>
<p>After field domains have been created, they can be assigned to fields in the database by right-clicking on the field name and selecting “Set Field Domain”:</p>
<p><img alt="" class="alignnone size-full wp-image-212453" height="273" src="/img/subscribers/north_road/qgis-3-28-improvements-for-working-with-esri-formats-and-services/assign_domain.webp" width="563"/></p>
<p>Field domains can also be viewed and managed by expanding out the “Field domains” option for each database.</p>
<h3>Relationship discovery</h3>
<p>Another exciting addition in QGIS 3.28 (and the underlying GDAL 3.6 release) is support for discovering database relationships in FileGeodatabases! (Once again, GeoPackage users also benefit from this, as we’ve implemented full support for GeoPackage relationships via the “<a href="http://www.geopackage.org/spec/related-tables/">Related Tables Extension</a>“).</p>
<p>Expanding out a database containing any relationships will show a list of all discovered relationships:</p>
<p><img alt="" class="alignnone size-full wp-image-212454" height="97" src="/img/subscribers/north_road/qgis-3-28-improvements-for-working-with-esri-formats-and-services/Screenshot-from-2022-11-24-12-54-51.webp" width="324"/></p>
<p>(You can view the full description and details for any of these relationships by opening the QGIS Browser “Properties” panel).</p>
<p>Whenever QGIS 3.28 discovers relationships in the database, these related tables will <strong>automatically</strong> be added to your project whenever any of the layers which participate in the relationship are opened. This means that users get the full experience as designed for these databases without <strong>any</strong> manual configuration, and the relationships will “just work”!</p>
<h3>Dataset Grouping</h3>
<p>Lastly, we’ve improved the way layers from FileGeodatabases are shown in QGIS, so that layers are now grouped according to their original dataset groupings from the database structure:</p>
<p><img alt="" class="alignnone size-full wp-image-212455" height="215" src="/img/subscribers/north_road/qgis-3-28-improvements-for-working-with-esri-formats-and-services/Screenshot-from-2022-11-24-13-15-06.webp" width="329"/></p>
<h2>Edit ArcGIS Online / Feature Service layers</h2>
<p>While QGIS has had read-only support for viewing and working with the data in ArcGIS Online (AGOL) vector layers and ArcGIS Server “feature service” layers for many years, we’ve added support for <strong>editing</strong> these layers in QGIS 3.28. This allows you to take advantage of all of QGIS’ easy to use, powerful editing tools and directly edit the content in these layers from within your QGIS projects! You can freely create new features, delete features, and modify the shape and attributes of existing features (assuming that your user account on the ArcGIS service has these edit permissions granted, of course). This is an exciting addition for anyone who has to work often with content in ArcGIS services, and would prefer to directly manipulate these layers from within QGIS instead of the limited editing tools available on the AGOL/Portal platforms themselves.</p>
<p>This new functionality will be available immediately to users upon upgrading to QGIS 3.28 — any users who have been granted edit capabilities for the layers will see that the QGIS edit tools are all enabled and ready for use without any further configuration on the QGIS client side.</p>
<h2>Filtering Feature Service layers</h2>
<p>We’ve also had the opportunity to introduce filter/query support for Feature Service layers in QGIS 3.28. This is a huge performance improvement for users who need to work with a subset of a features from a large Feature Service layer. Unfortunately, due to the nature of the Feature Service protocol, these layers can often be slow to load and navigate on a client side. By setting a SQL filter to limit the features retrieved from the service the performance can be dramatically increased, as only matching features will ever be requested from the backend server. You can use any SQL query which conforms to the subset of SQL understood by ArcGIS servers (see the Feature Service <a href="https://developers.arcgis.com/rest/services-reference/enterprise/query-feature-service-layer-.htm">documentation</a> for examples of supported SQL queries).</p>
<p> </p>
<p><img alt="" class="size-full wp-image-212369 aligncenter" height="797" src="/img/subscribers/north_road/qgis-3-28-improvements-for-working-with-esri-formats-and-services/Peek-2022-09-16-11-11.gif" width="1233"/></p>
<h2>What’s next?</h2>
<p>While QGIS 3.28 is an extremely exciting release for any users who need to work alongside ESRI software, we aren’t content to rest here! The exciting news is that in QGIS 3.30 we’ll be introducing a GUI driven approach allowing users to create new relationships in their FileGeodatabase (and GeoPackage!) databases.</p>
<p>At North Road we’re always continuing to improve the cross-vendor experience for both ESRI and open-source users through our continued work on the QGIS desktop application and our <a href="https://north-road.com/slyr/">SLYR</a> conversion suite. If you’d like to chat to us about how we can help your workplace transition from a fully ESRI stack to a mixed or fully open-source stack, just <a href="https://north-road.com/contact/">contact us</a> to discuss your needs.</p>
