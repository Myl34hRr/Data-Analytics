{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "ea792e1e-d980-40d2-85b5-ba7673b8fbe5",
   "metadata": {},
   "outputs": [],
   "source": [
    "from datetime import date, time, datetime, timedelta, timezone"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "eb3d15f1-602f-4a2d-8e2e-91c65d1e683d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Date: 2026-05-09\n"
     ]
    }
   ],
   "source": [
    "# date(year, month, day)\n",
    "today= date(2026, 5, 9)\n",
    "print(\"Date:\", today)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "a713ae56-f321-43c0-8c94-6c70983c283e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Time: 14:30:45\n"
     ]
    }
   ],
   "source": [
    "# time(hour, minute, secound, micorsecond)\n",
    "current_time = time(14, 30, 45)\n",
    "print(\"Time:\", current_time)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "1cc3515e-715d-41df-8d65-969641674eac",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Datetime: 2026-05-09 14:30:00\n"
     ]
    }
   ],
   "source": [
    "# datetime(year, month, day, hour, minute, second)\n",
    "current_datetime = datetime(2026, 5, 9, 14, 30)\n",
    "print(\"Datetime:\", current_datetime)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "f58a6619-7cab-4b1d-aaba-9763e2aae3c8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Futuer Date: 2026-05-16\n"
     ]
    }
   ],
   "source": [
    "# timedelta(days, hours, minutes, weeks, etc.)\n",
    "future_date = today + timedelta(days=7)\n",
    "print(\"Futuer Date:\", future_date)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "66187d93-5556-4873-b3d7-c1c3b8b694dd",
   "metadata": {},
   "outputs": [],
   "source": [
    "# timezone(timedelta(hours=offset))\n",
    "est = timezone(timedelta(hours=-5))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "47c1a4d3-3a89-4df1-a486-f6b5384c73c0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "UTC Time: 2026-05-14 01:06:26.416349+00:00\n"
     ]
    }
   ],
   "source": [
    "# datetime.now(timezone)\n",
    "utc_time = datetime.now(timezone.utc)\n",
    "print(\"UTC Time:\", utc_time)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "33d82ab8-9aee-49e6-be44-de13d3d7c678",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.14.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
