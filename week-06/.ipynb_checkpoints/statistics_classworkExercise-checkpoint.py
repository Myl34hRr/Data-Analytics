{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "c49c91a1-33b7-4195-a6f2-f256e0c5436a",
   "metadata": {},
   "outputs": [],
   "source": [
    "import statistics"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "7e32e6ed-64de-4467-9443-647c5c55cd30",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Sample dataset\n",
    "data = [10, 20, 20, 40, 50]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "5a333719-6464-4713-b616-bb0af26fe59b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "=== Python Statistics Module Demo ===\n",
      "\n"
     ]
    }
   ],
   "source": [
    "print(\"=== Python Statistics Module Demo ===\\n\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "bedd4d43-4335-4baf-92ea-f692d6e47730",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "mean: 28\n"
     ]
    }
   ],
   "source": [
    "# mean() average value\n",
    "print(\"mean:\", statistics.mean(data))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "724f3ff8-367a-49f1-b7c2-f3c6849a34c4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "medain: 20\n"
     ]
    }
   ],
   "source": [
    "# median() middle value\n",
    "print(\"medain:\", statistics.median(data))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "01b1cb46-e44f-4907-b1a0-411c14b706b6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "mode: 20\n"
     ]
    }
   ],
   "source": [
    "# mode() most common value \n",
    "print(\"mode:\", statistics.mode(data))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "d063ccca-a4f6-4608-a6a6-c8caf1fcdbde",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "stdev: 16.431676725154983\n"
     ]
    }
   ],
   "source": [
    "# stdev() standard deviation(sample)\n",
    "print(\"stdev:\", statistics.stdev(data))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "42c0b906-226e-46b0-8f7c-9b774e3601eb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "variance: 270\n"
     ]
    }
   ],
   "source": [
    "# variance() variance(sample)\n",
    "print(\"variance:\", statistics.variance(data))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1dd942f7-0779-4bc1-8a14-d398dfa980d4",
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
