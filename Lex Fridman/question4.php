<?php

function findLastKey(array $array, $value)
{
    $keys = [];
    foreach($array as $key=>$dict_value) {
        if(strcmp($value, $dict_value) == 0) {
            array_push($keys, $key);
        }
    }
    return end($keys);
}

echo findLastKey(array('Hello' => 'Green', 'World' => 'Blue'), 'Blue') . "\n";