from mock_builder import build_link_code_record, MockLinkType, build_holt_link_code_record, build_kronkite_link_code_record, build_pinwheel_link_code_record, build_hillmont_link_code_record, build_kourtney_link_code_record 
from datastore import DatastoreHandle

from random import choice
from string import ascii_letters, digits, ascii_uppercase

def generate_random_string(n):
  return ''.join(choice(ascii_letters + digits) for _ in range(n))

def generate_simple_random_string(n):
  return ''.join(choice(ascii_uppercase + digits) for _ in range(n))

def generate_curated_random_string(n):
  # omiting: 1, I, 0, O, Z, 2
  # since those characters are visually ambigious
  return ''.join(choice("ABCDEFGHJKLMNPQRSTUVWXY3456789") for _ in range(n))

def run():
  print("attempting create_link_code_record...")

  ds = DatastoreHandle()
  ds.create_link_code_record(build_kourtney_link_code_record(), generate_curated_random_string(8))

if __name__ == '__main__':
  run()
