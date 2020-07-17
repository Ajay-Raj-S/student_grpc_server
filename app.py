from flask import Flask, Response, request
import sys

from google.protobuf.json_format import MessageToJson
from client_wrapper import ServiceClient

import get_students_pb2_grpc as student_services
import get_students_pb2 as students_messages

app = Flask(__name__)
app.config['students'] = ServiceClient(student_services, 'StudentsStub', 'localhost', 50051)


@app.route('/')
def get_student_details():
	stud_id = request.args.get('id', 1)
	req = students_messages.get_student_id(student_id=int(stud_id))
	response = app.config['students'].StudentDetails(req)
	response = MessageToJson(response)
	print(response)
	return Response(response, content_type='application/json')


if __name__ == '__main__':
    app.run()

