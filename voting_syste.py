
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
    print(f"Vote cast for {candidate_name} by {voter_id}")
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
      print("Blockchain Voting System Menu")
      print("1.Add Candidate")
      print("2.Add Voter")
      print("3.Cast Vote")
      print("4.View Blockchain")
      print("5.Check Blockchain Validity")
      print("6.Exit")

      choice = input("Enter your choice (1-6):")

      if choice == '1':
          cid = input("Enter candidate ID:")
          name = input("Enter candidate name:")
          blockchain.add_candidate(cid, name)

      elif choice == '2':
          vid = input("Enter voter ID: ")
          name = input("Enter voter name: ")
          blockchain.add_voter(vid, name)

      elif choice == '3':
          vid = input("Enter your voter ID: ")
          cid = input("Enter candidate ID to vote for: ")
          blockchain.cast_vote(vid, cid)
      elif choice == '4':
          blockchain.print_blockchain()
      elif choice == '5':
          print("Blockchain valid:", blockchain.is_chain_valid())

      elif choice == '6':
          print("Exiting...")
          break  
      else:
          print("Invalid choice. Please enter a number from 1 to 6.")



if __name__ == "__main__":
  main()
