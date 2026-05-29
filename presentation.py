import tkinter as tk
import mediator as md


def button_clicked():

    address_block = {
        "street": inputs["street_input"],
        "city": inputs["city_input"],
        "state": inputs["state_input"],
        "zip": inputs["zip_input"]
    }

    geocode = md.getGeocode(address_block)

    message_label.config(text=geocode)


#Define window
root = tk.Tk()
root.title("My Location")


#Main frame that spans 4 columns
top_frame = tk.Frame(root, bg="lightblue", height=100)
top_frame.grid(row=0, column=0, columnspan=4, sticky="ew")

#Give the frame a visible size
top_frame.grid_propagate(False)

#Building frames
colors = ["red", "green", "yellow", "orange"]
frame_names = ["input_frame", "map1", "map2", "map3"]
frames = {}

for i in range(4):

    frames[frame_names[i]] = tk.Frame(
        root,
        bg=colors[i],
        width=100,
        height=100
    )

    frames[frame_names[i]].grid(row=0, column=i, padx=5, pady=5)

#input frame
field_names = ["street", "city", "state", "zip"]
labels ={}
row_frames = {}
inputs = {}

for i in range(len(field_names)):

    field_name = field_names[i]
    frame = frames["input_frame"]

    label_name = field_name + "_input_label"
    labels[label_name] = tk.Label(frame, text=field_name.capitalize() + ": ").grid(row=i, column=0, padx=5, pady=5, sticky="w") 

    input_name = field_name + "_input"
    inputs[input_name] = tk.Entry(frame)
    inputs[input_name].grid(row=i, column=1, padx=5, pady=5, sticky="w")


submit_button = tk.Button(frames["input_frame"], text="Submit", command=button_clicked).grid(row=len(field_names)+1, columnspan=2, pady=10)
message_label = tk.Label(frames["input_frame"], width=20, height=5).grid(row=len(field_names)+2, columnspan=2, pady=5)





root.mainloop()