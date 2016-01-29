Rails Go to Sass
================

Based on https://github.com/sporto/rails_go_to_spec

From a *.html.slim, *.html.erb, *.html.haml file this plugin will open the corresponding sass partial. E.g.:
```
/app/views/admin/pages/show.html.slim -> /app/assets/stylesheets/admin/pages/_show.sass
/app/views/admin/pages/_foo.html.haml -> /app/assets/stylesheets/admin/pages/_foo.sass
```

From a *.sass file it will attempt to find a matching view template or partial.

```
/app/assets/stylesheets/admin/pages/_show.sass -> /app/views/admin/pages/show.html.slim
                                                  /app/views/admin/pages/_show.html.slim
                                                  /app/views/admin/pages/show.html.haml
                                                  /app/views/admin/pages/_show.html.haml
                                                  /app/views/admin/pages/show.html.erb
                                                  /app/views/admin/pages/_show.html.erb
```

Installation
------------

Using Sublime Package Control
http://wbond.net/sublime_packages/package_control

Install rails_go_to_sass

Usage
-----
- Run from menu > Goto > Rails Go to Sass
- Default key binding is command + shift + u
- Or run from command palette 'Rails Go to Sass'
