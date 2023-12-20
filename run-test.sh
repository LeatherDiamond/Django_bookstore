#!/bin/bash
set -e

echo 'Waiting...'
sleep 25s

echo 'Runing Pytest'
pytest . -s

echo 'Success!'