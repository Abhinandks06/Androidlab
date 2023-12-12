package com.example.spinner;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Spinner;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {
    String names[]=new String[]{"item1","item2","item3","item4"};
    String items[]=new String[]{"item1.text","item2.text","item3.text","item4.text"};
    ArrayAdapter<String> adapter;
    Spinner spinner;
    TextView description;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
       spinner=findViewById(R.id.spinner);
       description=findViewById(R.id.description);
       adapter=new ArrayAdapter<String>(getApplicationContext(),android.R.layout.simple_list_item_1,names);
       spinner.setAdapter(adapter);
       spinner.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
           @Override
           public void onItemSelected(AdapterView<?> adapterView, View view, int i, long l) {
               switch (i){
                   case 0 : description.setText(""+items[i]);
                   break;
                   case 1 : description.setText(""+items[i]);
                   break;
                   case 2 : description.setText(""+items[i]);
                       break;
                   case 3 : description.setText(""+items[i]);
                       break;
               }
           }

           @Override
           public void onNothingSelected(AdapterView<?> adapterView) {

           }
       });

    }
}