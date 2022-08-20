from flask import Flask, render_template, request, redirect
from flask import Blueprint
from repositories import vet_repository
from repositories import pet_repository
from models.pet import Pet

vets_blueprint = Blueprint("vets",__name__)