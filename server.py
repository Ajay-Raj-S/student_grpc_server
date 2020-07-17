import grpc
import mysql.connector
from concurrent import futures
import time

import get_students_pb2_grpc as student_services
import get_students_pb2 as students_messages

mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "N0rmalu$er1171",
  database = "acedge"
)

class StudentService(student_services.StudentsServicer):

	def StudentDetails(self, request, context):
		metadata = dict(context.invocation_metadata())
		print(metadata)
		student_id = request.student_id
		mycur = mydb.cursor()
		mycur.execute("select student_fname, student_lname from students where student_id=%s", (student_id,))
		myres = mycur.fetchall()
		mycur.close()
		if len(myres) > 0:
			name = myres[0][0] + " " + myres[0][1]
			print(name)
			return students_messages.return_student_details(student_name=name)
		else:
			return students_messages.empty_student_details(student_details="Invalid StudentId")


def serve():
	server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
	student_services.add_StudentsServicer_to_server(StudentService(), server)
	print('Starting server. Listening on port 50051.')
	server.add_insecure_port('127.0.0.1:50051')
	server.start()
	try:
	    while True:
	        time.sleep(86400)
	except KeyboardInterrupt:
	    server.stop(0)


if __name__ == '__main__':
    serve()	