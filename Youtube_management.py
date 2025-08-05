import json


def load_data():
    try:
        with open("youtube.txt", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_data_helper(video):
    with open("youtube.txt", "w") as file:
        json.dump(video, file)


def list_all_videos(video):
    print("\n")
    print("=" * 70)
    for index, videos in enumerate(video, start=1):
        print(f"{index}. {videos['name']}, Duration: {videos['time']} ")
    print("\n")
    print("=" * 70)


def Add_video(video):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    video.append({"name": name, "time": time})
    save_data_helper(video)


def update_video(video):
    list_all_videos(video)
    index = int(input("Enter the video number to update: ").strip())
    if 1 <= index <= len(video):
       name = input("Enter the new video name: ").strip()
       time = input("Enter the new video time:").strip()
       video[index-1] = {'name':name, 'time':time}
       save_data_helper(video)
    else:
        print("Invalid index selected.")



def delete_video(video):
    list_all_videos(video)
    index = int(input("Enter video number to deleted: ").strip())
    if 1 <= index <= len(video):
        del video[index-1] 
        save_data_helper(video)
    else:
        print("Invalid vedio index selected. ")



def main():
    video = load_data()
    while True:
        print("\n Youtube Manager | choose an option")
        print("1. List a favourite vedio. ")
        print("2. Add a Youtube video.")
        print("3. Update a Youtube videos detail.")
        print("4. Delete a Youtube video.")
        print("5. Exit the app.")

        choose_option = input("Enter your opton: ").strip()
        if choose_option == "1":
            list_all_videos(video)

        elif choose_option == "2":
            Add_video(video)

        elif choose_option == "3":
            update_video(video)

        elif choose_option == "4":
            delete_video(video)

        elif choose_option == "5":
            print("Exiting..")
            break


if __name__ == "__main__":
    main()
