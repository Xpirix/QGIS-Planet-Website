---
source: "blog"
title: "Create a QGIS vector data provider in Python is now possible"
date: "2018-06-06T12:24:41+0000"
link: "https://www.itopen.it/qgis-vector-data-provider-python/"
draft: "false"
showcase: "planet"
subscribers: ["itopen"]
author: "ItOpen"
tags: ["gis", "qgis"]
languages: ["en_gb"]
available_languages: ["en_gb"]
---

<p> </p>
<h2>Why python data providers?</h2>
<p>My main reasons for having Python data provider were:</p>
<ul>
<li>quick prototyping</li>
<li>web services</li>
<li>why not?</li>
</ul>
<p> </p>
<p>This topic has been floating in my head for a while since I decided to give it a second look and I finally implemented it and merged for the next 3.2 release.</p>
<p> </p>
<h2>How it’s been done</h2>
<p>To make this possible I had to:</p>
<ul>
<li>create a public API for registering the providers</li>
<li>create the Python bindings (the hard part)</li>
<li>create a sample Python vector data provider (the boring part)</li>
<li>make all the tests pass</li>
</ul>
<p> </p>
<p>First, let me say that it wasn’t like a walk in the park: the Python bindings part is always like diving into woodoo and black magic recipes before I can get it to work properly.</p>
<p>For the Python provider sample implementation I decided to re-implement the memory (aka: scratch layers) provider because that’s one of the simplest providers and it does not depend on any external storage or backend.</p>
<p> </p>
<h2>How to and examples</h2>
<p>For now, the main source of information is the API and the tests:</p>
<ul>
<li>
<ul>
<li><a href="https://github.com/qgis/QGIS/blob/master/src/core/qgsproviderregistry.h#L188">https://github.com/qgis/QGIS/blob/master/src/core/qgsproviderregistry.h#L188</a></li>
<li><a href="https://github.com/qgis/QGIS/blob/master/tests/src/python/provider_python.py">https://github.com/qgis/QGIS/blob/master/tests/src/python/provider_python.py</a></li>
<li><a href="https://github.com/qgis/QGIS/blob/master/tests/src/python/test_provider_python.py">https://github.com/qgis/QGIS/blob/master/tests/src/python/test_provider_python.py</a></li>
</ul>
</li>
</ul>
<p>To register your own provider (<code>PyProvider</code> in the snippet below) these are the basic steps:</p>
<pre class="wp-code-highlight prettyprint">metadata = QgsProviderMetadata(PyProvider.providerKey(), PyProvider.description(), PyProvider.createProvider)
QgsProviderRegistry.instance().registerProvider(metadata)
</pre>
<p>To create your own provider you will need at least the following components:</p>
<ul>
<li>the provider class itself (subclass of <code>QgsVectorDataProvider</code>)</li>
<li>a feature source (subclass of <code>QgsAbstractFeatureSource</code>)</li>
<li>a feature iterator (subclass of <code>QgsAbstractFeatureIterator</code>)</li>
</ul>
<p>Be aware that the implementation of a data provider is not easy and you will need to write a lot of code, but at least you could get some inspiration from the existing example.</p>
<p> </p>
<p>Enjoy wirting data providers in Python and please let me know if you’ve fond this implementation useful!</p>
