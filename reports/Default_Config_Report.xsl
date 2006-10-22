<?xml version="1.0" encoding="iso-8859-1"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns="http://www.w3.org/1999/xhtml" version="1.0">
<xsl:output encoding="iso-8859-1" method="xml" doctype-public="-//W3C//DTD XHTML 1.0 Strict//EN" doctype-system="DTD/xhtml1-strict.dtd"/>
<xsl:template match="/SCTemplate">
<html>
<body>
<center><b>Config Report</b></center><br />
<center><b>Stats</b></center><hr />
<table cellspacing="10" cellpadding="0">
<tr><td>Str:</td><td><xsl:value-of select="Strength" /></td>
<td>Int:</td><td><xsl:value-of select="Intelligence"/></td>
<td>Hits:</td><td><xsl:value-of select="Hits" /></td></tr>
<tr><td>Con:</td><td><xsl:value-of select="Constitution" /></td>
<td>Pie:</td><td><xsl:value-of select="Piety" /></td>
<td>Power:</td><td><xsl:value-of select="Power" /></td></tr>
<tr><td>Dex:</td><td><xsl:value-of select="Dexterity" /></td>
<td>Cha:</td><td><xsl:value-of select="Charisma" /></td></tr>
<tr><td>Qui:</td><td><xsl:value-of select="Quickness" /></td>
<td>Emp:</td><td><xsl:value-of select="Empathy" /></td></tr>
</table><br />
<center><b>Resists</b></center><hr />
<table cellspacing="10" cellpadding="0">
<tr><td>Body:</td><td><xsl:value-of select="Body" /></td>
<td>Energy:</td><td><xsl:value-of select="Energy" /></td>
<td>Crush:</td><td><xsl:value-of select="Crush" /></td></tr>
<tr><td>Cold:</td><td><xsl:value-of select="Cold" /></td>
<td>Matter:</td><td><xsl:value-of select="Matter" /></td>
<td>Thrust:</td><td><xsl:value-of select="Thrust" /></td></tr>
<tr><td>Heat:</td><td><xsl:value-of select="Heat" /></td>
<td>Spirit:</td><td><xsl:value-of select="Spirit" /></td>
<td>Slash:</td><td><xsl:value-of select="Slash" /></td></tr>
</table><br />
<!--
<center><b>Skills</b></center><hr />


<skills/><br />
<center><b>Focus</b></center><hr />
<foci/><br />
<center><b>Cap Increases</b></center><hr />
<capbonuses/><br />
<center><b>Other Bonuses</b></center><hr />
<otherbonuses/><br />
<center><b>Piece Listing</b></center><hr />
<dl>
-->

<!-- FIXME - Document ordering or explicit?? -->
<xsl:for-each select="SCItem">
	<xsl:if test="count(SLOT) &gt; 0 and Equipped = '1'">
		<dt><b><xsl:value-of select="Location" /></b></dt>
		<xsl:choose>
			<xsl:when test="ActiveState = 'drop'">
				<dd>Name: <xsl:value-of select="Name"/></dd>
				<dd>Level: <xsl:value-of select="Level"/>&#160;
				Quality: <xsl:value-of select="ItemQuality"/>&#160;
				AF: <xsl:value-of select="AF"/>&#160;
				Bonus: <xsl:value-of select="Bonus"/></dd>
			</xsl:when>
			<xsl:otherwise>
				<dd>Imbue Points: <xsl:value-of select="format-number(UsedPoints, '##.0')"/> of 
					<xsl:value-of select="format-number(AvailPoints, '##.0')"/>
					Quality: <xsl:value-of select="ItemQuality"/>
					Overcharge: <xsl:value-of select="Overcharge"/></dd>
			</xsl:otherwise>
		</xsl:choose>
		<xsl:for-each select="SLOT">
			<xsl:variable name="slotnum">
				<xsl:value-of select="number(@Number) + 1"/>
			</xsl:variable>
			<xsl:if test="Type != 'Unused'">
				<xsl:choose>
					<xsl:when test="number(@Number) &lt;= 4 and ../ActiveState = 'player'">
						<dd>Gem <xsl:copy-of select="$slotnum"/>: <xsl:value-of select="Amount" />&#160;
							<xsl:value-of select="Effect" /> - <xsl:value-of select="Quality"/>&#160;
							<xsl:value-of select="GemName"/></dd>
					</xsl:when>
					<xsl:otherwise>
						<dd>Effect <xsl:copy-of select="$slotnum"/>: <xsl:value-of select="Amount"/> 
							&#160;<xsl:value-of select="Effect"/> 
						<xsl:if test="../ActiveState = 'player'">
							 - <xsl:value-of select="GemName"/>
						</xsl:if>
						</dd>
					</xsl:otherwise>
				</xsl:choose>
			</xsl:if>
		</xsl:for-each>
		<dd>Utility: <xsl:value-of select="Utility"/></dd>
	</xsl:if>
</xsl:for-each>
</body>
</html>
</xsl:template>
</xsl:stylesheet>
