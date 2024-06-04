#!/usr/bin/env bash
gunicorn factura_electronica.wsgi:application

