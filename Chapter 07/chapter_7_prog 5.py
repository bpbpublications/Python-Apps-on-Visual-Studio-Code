from threading import Condition, Thread
import random
patients = ['Sachin','Virat','Rohit']
doctors = ['Kapil','Sunil','Ravi']
class BookAppointment:
    def PatientRequest(self):
        condition_obj.acquire()
        print(f'Patient {random.choice(patients)} is waiting for the appointment')
        condition_obj.wait()  # Thread enters wait state
        print('Appointment Successfully Booked')
        condition_obj.release()

    def DoctorConfirm(self):
        condition_obj.acquire()
        print(f'Dr {random.choice(doctors)} is checking time for appointment!')
        time = random.randint(1, 9)
        print('Time Confirmed')
        print('Appointed Booked for {} PM'.format(time))
        condition_obj.notify() #communication made
        condition_obj.release()

condition_obj = Condition()
class_obj = BookAppointment()

TP = Thread(target=class_obj.PatientRequest)
TD = Thread(target=class_obj.DoctorConfirm)
TP.start()
TD.start()