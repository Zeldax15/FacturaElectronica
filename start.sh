#!/usr/bin/env bash
gunicorn FacturaElectronica.wsgi:application

