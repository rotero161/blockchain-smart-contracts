// Example of Smart Contract that give you an amount of ethers
// if you guess the random number that the contract generates

// The version of the solidity we are going to use
pragma solidity > 0.6.1 < 0.7.0

contract GuessNumber {

    address private player; // the address of the player that is going to play
    uint reward; // the amount of ethers that the player earn if they win
    uint randomNumberGenerated; // the random number that the contract will generate

    // The following line of code creates the function to execute the delivery of ethers
    event Number(uint randomNumberGenerated, uint guessedNumber, uint reward);

    // This function is used for comparing the random number and the number introduced by the player
    // It also assign the amount of reward
    function guess(uint guessedNumber) public payable { // The function is public (it can be consulted for everyone) and payable (it gives an amount of ethers)

        uint randomNumberGenerated = uint(keccak256(abi.encodePacked(now, msg.sender))) % 10 +1; // It generates the random number by using the hash of the previous block

        if(guessedNumber == randomNumberGenerated){

            player = msg.sender
            reward = 3000000000000000000; // Three ethers

        }

        emit Number(randomNumberGenerated, guessedNumber, reward) // Emit the reward if the number is guessed
    }
}