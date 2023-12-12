package com.example.intent;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.TextView;
import android.content.Intent;

public class MainActivity2 extends AppCompatActivity {
    TextView tv;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main2);
        Intent intent = getIntent();
        String user = intent.getStringExtra("user");
        String age = intent.getStringExtra("age");
        String text ="hello "+user+"age:"+age;
        tv = findViewById(R.id.textView);
        tv.setText(text);
    }
}