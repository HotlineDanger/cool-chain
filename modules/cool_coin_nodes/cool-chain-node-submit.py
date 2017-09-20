from flask import Flask
from flask import request
node = Flask(__name__)

# We store the transactions that this node contains in a list
nodes_transactions = []

@node.route('/txion', methods=['POST'])
def transaction():
    if request.method == 'POST':


