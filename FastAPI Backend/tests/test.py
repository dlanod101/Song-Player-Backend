import requests


BASE_URL = "http://127.0.0.1:8000/"

print("Creating a Song")
print(
    requests.post(
        f"{BASE_URL}/songs",
        json={
            "id": 1,
            "title": "Trial",
            "image": "Image url",
            "artiste": "Trialo Artiste",
            "is_liked": False,
            "audio_url": "Audio Url",
        },
    ).json()
)
print("Song Created", end="\n\n")

print("Creating a Song")
print(
    requests.post(
        f"{BASE_URL}/songs",
        json={
            "id": 2,
            "title": "Trial2",
            "image": "Image url2",
            "artiste": "Trialo Artiste2",
            "is_liked": False,
            "audio_url": "Audio Url2",
        },
    ).json()
)
print("Song Created", end="\n\n")

print("Getting songs")
print(requests.get(f"{BASE_URL}/list").json())
print("Songs gotten", end="\n\n")

print("Getting songs")
print(requests.get(f"{BASE_URL}/get/1").json())
print(requests.get(f"{BASE_URL}/get/2").json())
print("Songs gotten")

print("Updating song")
print(
    requests.put(
        f"{BASE_URL}/update/1",
        json={
            "id": 1,
            "title": "Updated Trial",
            "image": "Image url2",
            "artiste": "Trialo Artiste2",
            "is_liked": False,
            "audio_url": "Audio Url2",
        },
    ).json()
)
print("Songs gotten", end="\n\n")

print("Getting songs")
print(requests.get(f"{BASE_URL}/list").json())
print("Songs gotten")

print("Updating song")
print(
    requests.delete(
        f"{BASE_URL}/delete/1",
        json={
            "id": 1,
            "title": "Updated Trial",
            "image": "Image url2",
            "artiste": "Trialo Artiste2",
            "is_liked": False,
            "audio_url": "Audio Url2",
        },
    ).json()
)
print("Songs gotten", end="\n\n")

print("Getting songs")
print(requests.get(f"{BASE_URL}/list").json())
print("Songs gotten")

print("Deleting all songs")
print(requests.delete(f"{BASE_URL}/delete/").json())
print("Songs deleted", end="\n\n")

print("Getting songs")
print(requests.get(f"{BASE_URL}/list").json())
print("Songs gotten")

print("Creating a Song")
print(
    requests.post(
        f"{BASE_URL}/songs",
        json={
            "id": 3,
            "title": "Trial2",
            "image": "Image url2",
            "artiste": "Trialo Artiste2",
            "is_liked": False,
            "audio_url": "Audio Url2",
        },
    ).json()
)
print("Song Created", end="\n\n")

print("Creating a Song")
print(
    requests.post(
        f"{BASE_URL}/songs",
        json={
            "id": 4,
            "title": "Trial2",
            "image": "Image url2",
            "artiste": "Trialo Artiste2",
            "is_liked": False,
            "audio_url": "Audio Url2",
        },
    ).json()
)
print("Song Created", end="\n\n")

print("Creating a Song")
print(
    requests.post(
        f"{BASE_URL}/songs",
        json={
            "id": 5,
            "title": "Trial2",
            "image": "Image url2",
            "artiste": "Trialo Artiste2",
            "is_liked": False,
            "audio_url": "Audio Url2",
        },
    ).json()
)
print("Song Created", end="\n\n")

print("Creating a Song")
print(
    requests.post(
        f"{BASE_URL}/songs",
        json={
            "id": 6,
            "title": "Trial2",
            "image": "Image url2",
            "artiste": "Trialo Artiste2",
            "is_liked": False,
            "audio_url": "Audio Url2",
        },
    ).json()
)
print("Song Created", end="\n\n")

print("Deleting songs")
print(
    requests.delete(f"{BASE_URL}/select_delete/", json=[3, 4]).json()
)
print("Songs deleted", end="\n\n")

print("Getting songs")
print(requests.get(f"{BASE_URL}/list").json())
print("Songs gotten")