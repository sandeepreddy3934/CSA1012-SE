# Attendance Management Module

def display_attendance():
    total_classes = 20
    attended_classes = 18

    percentage = (attended_classes / total_classes) * 100

    print("Total Classes:", total_classes)
    print("Attended Classes:", attended_classes)
    print("Attendance Percentage:", percentage, "%")

display_attendance()
