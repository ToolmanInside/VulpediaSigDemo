pragma solidity ^0.4.25;

contract ERC20 {}

contract buy1 {

    function transfer(address target, uint value) public payable
    {
        target.transfer(value);
    }

    function buy(ERC20 _token, address[] _exs, uint[] _indexs) public payable {
        for (uint i = 0; i < _exs.length; i++)
        {
            bytes memory data = new bytes(_indexs[i+1] - _indexs[i]);
            require(_exs[i] != address(0));
            transfer(_exs[i], 10);
        }
    }
}