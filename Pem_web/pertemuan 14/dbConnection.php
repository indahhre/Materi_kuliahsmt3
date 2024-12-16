<?php
$connect = mysqli_connect("localhost", "root", "", "sikampus");
if (!$connect) {
    die("koneksi gagal: " . mysqli_connect_error());
} else {
    echo "koneksi berhasil";
}