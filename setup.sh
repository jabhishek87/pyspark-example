#!/bin/bash


usage(){
    cat <<OUT

$(basename $0): a simple shell script to  download movie datasets

Usage: 
    $(basename $0)

Options:
    -d            Download datasets
    -u            unzip datasets
    -a            download and unzip datastes
    -r            install python dependencies

OUT
exit 1
}


download_data() {
    echo "Downloading data"
    wget http://files.grouplens.org/datasets/movielens/ml-20m.zip -O datasets.zip
}

unzip_data() {
    echo "unzip datasets"
    PWD=$(pwd)
    unzip datasets.zip
}

install_depedencies() {
    echo "resolving python dependiencies"
    pip install -r requirements.txt
}


while getopts ":dur" opt; do
  case $opt in
    d) download_data && exit 0;;
    u) unzip_data && exit 0;;
    r) install_depedencies && exit 0;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      usage
      ;;
  esac
done

usage
