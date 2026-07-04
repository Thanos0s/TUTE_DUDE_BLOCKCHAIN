from os import name
import hashlib
import time

class Block:
  def __init__(self,index,voter_id,previous_hash,time_stamp,data,hash):
    self.index = index
    self.voter_id = voter_id
    self.previous_hash = previous_hash
    self.time_stamp = time_stamp
    self.data = data
    self.hash = hash
    self.hash=self.calculate_hash()


  def calculate_hash(self):
    value = str(self.index) + str (self.time_stamp) + self.voter_id + self.previous_hash + str(self.data)
    return hashlib.sha256(value.encode()).hexdigest()

# voter class
class Voter:
  def __init__(self,voter_id,name):
    self.voter_id=voter_id
    self.name=name
    self.has_voted = False

# candidate class
class Candidate:
  def __init__(self,candidate_id,name):
    self.candidate_id=candidate_id
    self.name=name

class Blockchain:
  def __init__(self):
    self.chain = [self.create_gensis_block()]
    self.voters= {}
    self.candidates= {}

  def create_gensis_block(self):
    return Block(0, "Genesis", "0", time.time(), "Genesis Block Data", "")
  def get_latest_block(self):
     return self.chain[-1]


  def add_candidate(self,candidate_id,name):
    if candidate_id in self.candidates:
      print("Candidate ID already exists")
      return False
    self.candidates[candidate_id]= Candidate(candidate_id,name)
    print(f"Candidate added: {candidate_id} - {name}")
    return True

  #
  def add_voter(self, voter_id, name):
    if voter_id in self.voters:
        print("Voter ID already exists.")
        return False
    self.voters[voter_id] = Voter(voter_id, name)
    print(f"Voter added: {voter_id} - {name}")
    return True

  def cast_vote(self, voter_id, candidate_id):
    if voter_id not in self.voters:
        print("Voter not found. Please add the voter first.")
        return False
    if candidate_id not in self.candidates:
        print("Candidate not found.")
        return False
    if self.voters[voter_id].has_voted:
        print("Voter already voted! Double voting is not allowed.")
        return False

    candidate_name = self.candidates[candidate_id].name
    latest_block = self.get_latest_block()
    new_block = Block(len(self.chain),voter_id,latest_block.hash,time.time(),candidate_name, "")
    self.chain.append(new_block)
    self.voters[voter_id].has_voted = True
    print(f"Vote casr for {candidate_name} by {voter_id}")
    return True

  def is_chain_valid(self):
    for i in range(1,len(self.chain)):
      current_block = self.chain[i]
      previous_block = self.chain[i-1]

      if current_block.hash!= current_block.calculate_hash():
        return False
      if current_block.previous_hash != previous_block.hash:
        return False
    return True

  def count_voters(self):
    results ={}
    for cid in self.candidates:
      results[self.candidates[cid].name] = 0
    for block in self.chain[1:]:
      if block.data in results:
        results[block.data] +=1
    return results

  def print_blockchain(self):
      print("\nBlockchain Details")
      for block in self.chain:
          print(f"Index:{block.index}")
          print(f"Voter ID:{block.voter_id}")
          print(f"Candidate:{block.data}")
          print(f"Hash: {block.hash}")
          print(f"Previous Hash:{block.previous_hash}")
          

def main():
  blockchain = Blockchain()

  while True:
      print("\n VOTER ID")
      PRINT("\n candidate ID")
      #print("\n")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            cid = input("Enter candidate ID: ")
            name = input("Enter candidate name: ")
            blockchain.add_candidate(cid, name)

        elif choice == "2":
            vid = input("Enter voter ID: ")
            name = input("Enter voter name: ")
            blockchain.add_voter(vid, name)

        elif choice == "3":
            vid = input("Enter your voter ID: ")
            cid = input("Enter candidate ID to vote for: ")
            blockchain.cast_vote(vid, cid)

        elif choice == "4":
            blockchain.print_blockchain()

        elif choice == "5":
            print("Blockchain valid:", blockchain.is_chain_valid())

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a numberfrom 1 to 6.")


if __name__ == "__main__":
    main()
