#!/bin/bash
cd $(dirname $0)
sass gameapp/static/sass/main.scss > gameapp/static/css/main.css
