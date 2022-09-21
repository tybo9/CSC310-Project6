## Ayoub Rammo
##CS 310
#ha6
def presidentcandidate(voters):
  voters.sort()  # this is sorting for voters
  counts = 1
  s_counts = 0
  ID = voters[0]
  s_ID = -1

  for i in range(1, len(voters)): #loop

    if voters[i] == voters[i - 1]:  # for voters that have the same Unique ID
      counts = counts + 1
    else:
      if s_counts < counts:     # checking previous Unique ID
        s_counts = counts
        s_ID = ID
        counts = 1

        ID = voters[i]
  if counts > s_counts:        # this will check the last unique ID
    s_counts = counts
    s_ID = voters[len(voters)-1] #loop

  return s_ID  ## calling back that function
print("the Unique ID is:- ", presidentcandidate([10, 874, 10, 874, 92,384, 92,874,10,10]))
