#version 330 core

in vec2 uv;
uniform float iTime;
uniform vec2 iResolution;
uniform vec2 iMouse;
out vec4 frag_color;


vec3 palette(float t, vec3 a, vec3 b, vec3 c, vec3 d)
{
    return a + b*cos(6.28318*(c*t+d));
}

void main()
{	
    vec2 UV = (uv-0.5)*2;
    vec2 uv0 = UV;
    vec3 finalColor = vec3(0.0);

    for(float i = 0.0; i < 4.0; i++){
        UV = fract(UV*1.5)-0.5;

        float d = length(UV) * exp(-length(uv0));

        vec3 col = palette(length(uv0) + i*.4 +iTime*.4, vec3(0.5), vec3(0.5), vec3(1.0), vec3(0.263, 0.416, 0.557));

        d = sin(d*8.0 + iTime)/8.0;
        d = abs(d);

        // d = 0.01/d;
        d = pow(0.01 / d, 1.2);

        finalColor += col * d;
    }

	frag_color = vec4(finalColor, 1.0);
}